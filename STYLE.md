# My Style Guide

> Learned on 2026-11-26 from 9 reference videos in `references/` (reference8.mp4 was an incomplete download and was skipped).
> The theme across them: **history storytelling.** A host talks to camera, and archival photos, maps and old newspapers cover most of the runtime.
> Short vertical videos (reference3, 4, 5) set the editing rules. The long horizontal ones (1, 2, 6, 7, 9, 10) add ideas for B-roll, titles and graphics.
> Numbers come from ffmpeg cut detection and frame stills. Speech was not transcribed in this pass, so wording rules are based on the on-screen captions.
> Claude adds your feedback to **Do / Don't** after each edit, so the style improves over time.

## Format
- Aspect ratio / resolution: 9:16, 1080x1920
- Frame rate: 24 fps (ref: reference3, reference5). Use 30 fps only if the raw footage is 30 and would stutter (ref: reference4).
- Typical length: 60-100 seconds (ref: reference3 = 0:59, reference4 = 1:42, reference5 = 1:42)

## Hook (first 3 seconds)
- How the video opens: with a question or a surprising claim from the host, said within the first second, then straight into B-roll that shows it (ref: reference3 @ 0:00 "Where did the idea of an eight-hour work day come from?"; reference4 @ 0:00 "What if I told you...")
- On-screen text in the hook: optional headline at the top for the whole video. Use 2 lines, white box with black bold text, about 44px at 1080 wide, centered at about 15% from top (ref: reference4 @ 0:00-0:10). Name the subject with a small white label above the captions the first time they come up (ref: reference4 @ 0:00 "Bessie Blount Griffin").
- Cuts in the first 3 seconds: 2 (talking head to B-roll by about 0:01, then a second B-roll at about 0:02) (ref: reference3 @ 0:00-0:03, reference4 @ 0:01)

## Pacing
- Average shot length: about 3 seconds (reference3 = 3.1s, reference5 = 3.3s). Never hold one image more than 5 seconds without a zoom or a cut.
- Pauses kept between sentences: none. Cut every silence longer than 0.3s. ffmpeg found no silences over 0.4s in the shorts (ref: reference3, 4, 5).
- Jump cut style: hard cuts, alternating between a wide and a tight (punch-in) talking-head frame, with B-roll covering about 60-70% of the runtime (ref: reference3 @ 0:12-0:20, reference5 throughout)

## Captions
- Font / weight: heavy geometric sans-serif such as Montserrat ExtraBold or Black
- Size (px at 1080 wide): about 65px cap height
- Position (% from top): 62-70% (just below the face, never covering the mouth)
- Words per line / words on screen at once: 1-3 words, one line
- Colors (text / outline / highlight word): white text with a soft dark shadow. The word being spoken gets a rounded **indigo box (#5B5BE6)** behind it (ref: reference4, reference5 throughout).
  Alternative: all yellow (#FFE600) bold italic with a thin black outline and no box (ref: reference3).
- Animation (pop, fade, none): word-by-word. The highlight box jumps to each word as it's spoken, with no fade.
- All caps?: yes

## Zooms & framing
- Punch-in amount and how often: tight crop about 130-150% on every other talking-head shot (ref: reference3 @ 0:12 vs 0:16, reference5 @ 0:20 vs 0:28)
- Archival stills: slow Ken Burns push-in, about 5% over the shot (ref: reference1, reference6 @ 0:15)
- Framing of the speaker: chest-up and centered, with eyes about 35% from the top. Use a warm, softly blurred background (ref: reference3, reference5).

## Graphics & text
- Horizontal photos in a vertical frame: put the photo full width and fill above and below with a blurred, darker copy of the same image (ref: reference5 @ 0:00-0:10)
- Split screen: host on the top half, archival image on the bottom half, for 2-4 seconds when explaining a picture (ref: reference3 @ 0:12, reference5 @ 0:40)
- Maps: zoom into a real map with a red pin on the place being discussed (ref: reference4 @ 0:20, reference1 @ 1:00)
- Old newspaper headlines as full-screen B-roll for dramatic claims (ref: reference6 @ 0:00)
- Date and place card: small spaced caps such as "1892 / CARTER COUNTY, TENNESSEE" over a landscape shot (ref: reference6 @ 0:33)
- Titles / lower thirds: name on a white rectangle with black bold text, and their role underneath in smaller text (ref: reference7 @ 0:33, reference4 @ 0:00)
- Emojis, icons, stickers: none
- Tool to use (Remotion / HyperFrames): HyperFrames for captions and lower thirds. Remotion only for map zooms and split screens.

## Transitions
- Hard cuts only in shorts (ref: reference3, 4, 5). Save slide or parallax transitions for long-form (ref: reference9).

## Color
- Overall look: warm and moody on the host, with an amber or brown background glow and medium contrast (ref: reference3, reference5). Archival photos stay black and white. Don't colorize them.

## Music & sound effects
- Music type and energy: not measured in this pass. Default to a quiet, low-key documentary bed (soft piano or strings).
- Music level under voice: about -25 dB under the voice, so speech always leads
- Sound effects: a light whoosh on map zooms. Don't add pops on captions, because none of the references use them.
- Final loudness: -14 LUFS. The references ranged from -26 to -15, so normalize every export.

## Ending
- End on the host's last line with a hard cut. No outro card. Optional one-line spoken call to action ("Follow for more forgotten history") over the final shot (ref: reference3, reference4).

## Do / Don't
*Your corrections, saved as rules. Never deleted, only added to or refined.*

**Do**
- Show a picture of whatever is being named (a person, place or document) within 1 second of saying it
- Keep every shot under 5 seconds in shorts

**Don't**
- Don't copy other creators' logos, title graphics, channel names or catchphrases. That includes scroll title cards, neon channel signs and network watermarks seen in the references.
- Don't leave pauses or "um"s in

## References studied
| Video | Creator | Link | What I took from it |
|---|---|---|---|
| reference3.mp4 | unknown | local file | Question hook, 3s shots, yellow word captions, punch-ins, split screen |
| reference4.mp4 | unknown | local file | Top headline bar, name label, indigo highlight captions, map with pin |
| reference5.mp4 | unknown | local file | Blurred-fill archival photos, warm host lighting, fast B-roll |
| reference1.mp4 | unknown | local file | Sentence-length quote text over faded photos, map B-roll (long-form) |
| reference2.mp4 | unknown | local file | Bold all-caps captions on a long video, 3s average shot |
| reference6.mp4 | unknown | local file | Newspaper headline cold open, date and place card, picture-in-picture |
| reference7.mp4 | unknown | local file | Clean lower third (name and outlet) |
| reference9.mp4 | unknown | local file | Paper-collage, parallax motion graphics (long-form only) |
| reference10.mp4 | unknown | local file | Portrait-heavy B-roll, mixing film clips with paintings |
| reference8.mp4 | — | local file | Skipped: file is incomplete (299 KB, won't open) |
