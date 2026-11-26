---
name: learn-style
description: Download 3-5 reference videos with yt-dlp, analyze their editing style, and write STYLE.md. Use when the owner shares links to videos whose look or pacing they want.
argument-hint: "[3-5 video links]"
---

# Learn a style from reference videos

Links: $ARGUMENTS
If no links were given, ask for 3-5 links to short videos (Reels, TikToks or Shorts) whose editing style the owner likes.

## 1. Download (small files only, the laptop is short on space)
For each link:
`yt-dlp -f "bv*[height<=720]+ba/b[height<=720]" -o "references/%(uploader)s - %(title).60s [%(id)s].%(ext)s" <link>`
Also save the auto-captions if available (`--write-auto-subs --sub-langs en --sub-format srt`).
Only download public videos the owner chose. These are for study only and are never reposted.

## 2. Analyze each video
- Transcribe it: `python tools/transcribe.py "<file>" --model base`
- Find the cuts: `ffmpeg -i "<file>" -vf "select='gt(scene,0.3)',showinfo" -f null - 2>&1` and read the `pts_time` values.
  Work out the average shot length and the number of cuts in the first 3 seconds.
- Grab stills: one every 2 seconds plus the first 3 seconds frame by frame
  (`ffmpeg -i "<file>" -vf fps=0.5 _work/ref-<id>/frame_%03d.jpg`). Look at them to judge caption look, framing and color.
- Audio: measure loudness (`ffmpeg -i "<file>" -af ebur128 -f null -`) and note music, sound effects and silence.

## 3. Write STYLE.md
Fill in every section of the existing `STYLE.md` template. Rules:
- Each rule must be **specific and measurable**. Write "captions: 2-3 words at a time, white bold
  sans-serif, about 80px at 1080 width, centered at 65% screen height, yellow on the key word", not "punchy captions".
- **Cite the source** for each rule: `(ref: <uploader> @ 0:04)`.
- Where the references disagree, choose one approach and note the alternative.
- **Inspire, don't copy:** describe techniques, never copy logos, watermarks, catchphrases or exact graphics.
- Keep the existing "Do / Don't" section and add to it. Never delete the owner's corrections.

## 4. Finish
Delete the `_work/ref-*` frame folders to save space, but keep the reference videos.
Show the owner a short plain-English summary (5-8 bullets) of the style you found and ask:
"Does this sound like what you want? Tell me anything to change."
Apply the changes they ask for, then save to GitHub.
