"""
Transcribe a video or audio file with word-level timestamps.

Usage (from the project folder):
    python tools/transcribe.py "raw-footage/my clip.mp4"
    python tools/transcribe.py "raw-footage/my clip.mp4" --model medium
    python tools/transcribe.py "raw-footage/my clip.mp4" --clip 5     # only first 5 seconds (for testing)

Writes three files into _work/<clip name>/ :
    transcript.json   every word with start/end time and confidence (used for cut lists + captions)
    transcript.srt    normal subtitle file, one line per sentence
    transcript.txt    plain readable text with timestamps
Also lists pauses over 0.4s and likely filler words, which /rough-cut uses.

Models are downloaded once into the models/ folder (on the external drive, not the laptop).
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
FILLERS = {"um", "uh", "uhm", "umm", "er", "erm", "ah", "hmm", "mm", "like", "basically",
           "actually", "literally", "so", "you know", "i mean", "kind of", "sort of"}
STRONG_FILLERS = {"um", "uh", "uhm", "umm", "er", "erm", "ah", "hmm", "mm"}


def fmt_srt(t: float) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def extract_audio(src: Path, dst: Path, clip_seconds):
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", str(src)]
    if clip_seconds:
        cmd += ["-t", str(clip_seconds)]
    cmd += ["-vn", "-ac", "1", "-ar", "16000", str(dst)]
    subprocess.run(cmd, check=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("file")
    p.add_argument("--model", default="small", help="tiny, base, small (default), medium, large-v3")
    p.add_argument("--language", default=None, help="e.g. en. Leave empty to auto-detect")
    p.add_argument("--clip", type=float, default=None, help="only transcribe the first N seconds")
    p.add_argument("--out", default=None, help="output folder (default _work/<clip name>)")
    args = p.parse_args()

    src = Path(args.file)
    if not src.exists():
        sys.exit(f"File not found: {src}")

    try:
        from faster_whisper import WhisperModel
    except ImportError:
        sys.exit("faster-whisper is not installed. Run: python -m pip install faster-whisper")

    out = Path(args.out) if args.out else PROJECT / "_work" / src.stem
    out.mkdir(parents=True, exist_ok=True)
    models_dir = PROJECT / "models"
    models_dir.mkdir(exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        wav = Path(tmp) / "audio.wav"
        print("Extracting audio...")
        extract_audio(src, wav, args.clip)

        print(f"Loading Whisper model '{args.model}' (first time downloads it to models/)...")
        model = WhisperModel(args.model, device="cpu", compute_type="int8",
                             download_root=str(models_dir))

        print("Transcribing (this can take a few minutes on a laptop)...")
        segments, info = model.transcribe(
            str(wav), language=args.language, word_timestamps=True,
            vad_filter=False,  # keep pauses + fillers visible so we can decide what to cut
            condition_on_previous_text=False,
            # Whisper normally hides "um"/"uh"; this prompt nudges it to write them down
            initial_prompt="Umm, let me think like, hmm... Okay, here's what, uh, I'm thinking.",
        )

        words, segs = [], []
        for seg in segments:
            seg_words = []
            for w in seg.words or []:
                item = {"word": w.word.strip(), "start": round(w.start, 3),
                        "end": round(w.end, 3), "prob": round(w.probability, 3)}
                words.append(item)
                seg_words.append(item)
            segs.append({"start": round(seg.start, 3), "end": round(seg.end, 3),
                         "text": seg.text.strip(), "words": seg_words})

    # Pauses and filler words
    pauses = []
    for a, b in zip(words, words[1:]):
        gap = round(b["start"] - a["end"], 3)
        if gap > 0.4:
            pauses.append({"after_word": a["word"], "start": a["end"], "end": b["start"], "length": gap})
    fillers = []
    for w in words:
        clean = re.sub(r"[^a-z' ]", "", w["word"].lower()).strip()
        if clean in FILLERS:
            fillers.append({**w, "strong": clean in STRONG_FILLERS})

    data = {"source": str(src), "language": info.language, "duration": round(info.duration, 3),
            "model": args.model, "segments": segs, "words": words,
            "pauses_over_0_4s": pauses, "possible_fillers": fillers}
    (out / "transcript.json").write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    with open(out / "transcript.srt", "w", encoding="utf-8") as f:
        for i, s in enumerate(segs, 1):
            f.write(f"{i}\n{fmt_srt(s['start'])} --> {fmt_srt(s['end'])}\n{s['text']}\n\n")

    with open(out / "transcript.txt", "w", encoding="utf-8") as f:
        for s in segs:
            f.write(f"[{s['start']:7.2f} - {s['end']:7.2f}] {s['text']}\n")

    print(f"\nDone. {len(words)} words, {len(pauses)} pauses > 0.4s, {len(fillers)} possible fillers.")
    print(f"Saved to: {out}")


if __name__ == "__main__":
    main()
