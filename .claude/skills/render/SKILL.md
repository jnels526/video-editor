---
name: render
description: Apply the approved cut list, then add captions, graphics and music following STYLE.md, run quality checks and export a 9:16 video to exports/. Use after /rough-cut has been approved.
argument-hint: "[optional: clip name]"
---

# Render with style

## 0. Check
Find `_work/<clip>/cutlist.json`. If it's missing or not `"approved": true`, **stop** and suggest `/rough-cut`.
Read `STYLE.md` in full. If it's empty, ask whether to use simple defaults (white captions, no music) or run `/learn-style` first.

## 1. Assemble the cuts (FFmpeg)
- Cut each KEEP segment from the original into `_work/<clip>/`, re-encoding for frame accuracy (no stream copy).
- Join the segments with **2-4 frame audio crossfades** (`acrossfade`) so there are no pops. Hard cuts on the picture are fine unless STYLE.md says otherwise.
- Reframe to **9:16, 1080x1920**: crop the center (or follow the subject if STYLE.md says to). Never stretch the picture.
- Re-transcribe the assembled video (`tools/transcribe.py`) so caption timing matches the new edit.

## 2. Style (Remotion and/or HyperFrames)
Follow STYLE.md exactly:
- **Captions**: word-timed from the new transcript, using the font, size, position, words per line and highlight style from STYLE.md.
  Keep them inside the safe zone: away from the top 250px, the bottom 400px and the right 150px, where the app's buttons sit.
- **Zooms, punch-ins, graphics, titles, transitions**: use Remotion for captions and layouts that change with the transcript,
  and HyperFrames for one-off animated graphics and title cards.
- **Music**: only from `assets/`. Duck it under the voice (sidechain compression or about -18 to -22 dB under speech).
  If `assets/` has no music, ask the owner instead of adding any.
- **Hook**: make the first 3 seconds match the hook rules in STYLE.md.

## 3. Final mix
Mix to **-14 LUFS integrated, true peak no higher than -1 dBTP** (`loudnorm`, two passes).
Export H.264 at high quality, AAC 320k, 30fps (or the source frame rate).

## 4. Quality check before showing the owner
- **Caption sync**: compare a sample of caption timings with the transcript. Off by more than 2 frames fails.
- **Safe zones**: grab stills (`_work/<clip>/qc/`) at the hook, 25%, 50%, 75% and the end, and check that nothing sits under the app buttons.
- **Audio pops/clicks**: listen at every join (check for sudden jumps in level) and check the final loudness reading.
- **Flash frames**: no 1-2 frame leftovers at the cut points.
- Fix any failures before moving on.

## 5. Export and show
Save to `exports/<clip name> - v<N>.mp4` (never overwrite an earlier version).
Show the owner the 5 QC stills, the final cut list, the length, the loudness and the file location.
Ask: **"Watch it and tell me what to change, in your own words."**
Turn each piece of feedback into a general rule in the STYLE.md "Do / Don't" section, re-render as v<N+1>, and repeat.

## 6. Clean up
When the owner is happy, offer to delete `_work/<clip>/` to free space (the transcript can be kept if they like).
Save to GitHub (text files only). Suggest `/save-workflow` if this is one of the first few edits.
