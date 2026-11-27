---
name: rough-cut
description: Transcribe the newest clip in raw-footage with word-level timestamps and propose a cut list (filler words, retakes, false starts, long pauses). Always stops and waits for approval. Use when the owner drops in new footage or asks for a first cut.
argument-hint: "[optional: file name]"
---

# Rough cut with an approval gate

## 1. Pick the clip
$ARGUMENTS may hold a style name (`gym`, `travel`, `history` or any file in `styles/`) and/or a file name.
Use the file if given, otherwise the newest video in `raw-footage/` (including its subfolders). Tell the owner which file you're using.

**Pick the style** (see CLAUDE.md rule 6): the style named in $ARGUMENTS, otherwise the clip's subfolder
(`raw-footage/gym/` means `styles/gym.md`), otherwise ask. Say: "Using the **<style>** style."
Read `styles/<style>.md` before choosing cuts.
**Never change the original.** Everything goes in `_work/<clip name>/`.

## 2. Transcribe
`python tools/transcribe.py "raw-footage/<file>"` (small model). Read `transcript.json`.
Also get the frame rate and length: `ffprobe -v error -show_entries stream=r_frame_rate,width,height:format=duration "<file>"`.

## 3. Find what to cut
- **Filler words**: um, uh, er and similar ("strong" fillers). Cut "like", "so" and "you know" only when they add nothing.
- **Retakes**: when the same idea is said twice or more, **keep the best take, not the latest**.
  "Best" means fewest stumbles, clearest wording and most energy. Explain why you chose it.
- **False starts**: sentences that are abandoned and restarted.
- **Pauses over 0.4s**: shorten them to about 0.15s. Don't remove them completely, or the speech sounds robotic.
- Dead air at the start and end: the video starts on the first word of the hook.
- Follow the pacing rules in `styles/<style>.md`.
- **Little or no speech** (a gym set, travel footage): the transcript can't drive the cuts. Instead, pick the strongest moments
  (the hardest rep, the best view, clear movement) using stills every 0.5s and scene detection, and trim dead time between them.
  Match the shot lengths in the style file, and mark these cuts "visual" in the Reason column.

## 4. Cutting rules
- Never cut mid-word. Cut points sit in the gap between words, ideally at a breath or sentence end.
- Leave about 0.05s of handle before a word starts and after it ends, so consonants aren't clipped.
- Snap every cut point to the nearest frame.

## 5. Show the cut list and STOP
Save `_work/<clip>/cutlist.json` (`"style": "<style>"` plus a list of segments to KEEP: `in`, `out` in seconds) and show the owner a table:

| # | Remove from → to | What's said | Reason | Confidence |
|---|---|---|---|---|

Then show:
- Length before → after
- A readable "after" script (the transcript with cuts applied)
- Anything you weren't sure about, marked **low confidence**

End with: **"Reply 'approved' or tell me what to change (e.g. 'keep #4', 'cut the part about X')."**
**Do not render anything until the owner approves.** Update the cut list for each change and show it again.
When approved, mark `"approved": true` in `cutlist.json` and say: "Run /render when you're ready."
