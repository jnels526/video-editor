# AI Video Editor: rules for Claude

This folder is a video editing workspace. The owner is **not technical**. Explain things
in plain English, give one step at a time, and never assume they know Git or the terminal.

## Machine
- Windows laptop with **little free disk space**.
- This project folder lives on the external drive **"My Passport"**. Check its drive letter
  in File Explorer or with `Get-Volume`. **Don't hard-code a letter.** Use paths relative to this folder.
- Use PowerShell commands, not bash, unless Git Bash is clearly available.

## Folders
| Folder | Contents | In GitHub? |
|---|---|---|
| `raw-footage/` | Original clips from the owner (optionally in `gym/`, `travel/`, `history/` subfolders) | No |
| `references/<style>/` | Videos whose style the owner likes, one subfolder per style (downloaded with yt-dlp) | No |
| `styles/` | One style guide per kind of video: `history.md`, `gym.md`, `travel.md` | Yes |
| `assets/` | Music, sound effects, fonts, logos | No |
| `exports/` | Finished videos | No |
| `_work/` | Scratch space: transcripts, cut lists, test renders. Create it if it doesn't exist | No |
| `models/` | Whisper model files | No |
| `remotion/` | Remotion project code (graphics and captions) | Yes (code only) |
| `tools/` | Helper scripts | Yes |

## Hard rules
1. **Never modify, move, rename or delete anything in `raw-footage/`.** Read from it and write copies to `_work/`.
2. **Never add video, audio, images or fonts to Git.** `.gitignore` already blocks them. Never use `git add -f`.
3. **Approval gate:** always show the cut list and wait for the owner's "approved" before rendering.
4. **Transcribe before cutting.** Cuts on speech are based on word timestamps, never guessed from waveforms alone.
   Clips with little or no speech (gym sets, travel footage) are cut on movement and the music beat instead; say so in the cut list.
5. Never cut in the middle of a word. Cut on breaths, pauses or sentence ends.
6. **Pick one style for every edit** and follow it for every creative choice. The styles live in `styles/`.
   Use the style the owner names. Otherwise use the subfolder the clip is in (`raw-footage/gym/` means `styles/gym.md`).
   Otherwise ask which style to use, listing the files in `styles/`. Always tell the owner which style you're using.
   If that style file is still empty, say so and suggest `/learn-style <style>`.
   Always also follow `styles/storytelling.md` (character, tension, payoff; peak-moment hooks; story loops).
7. **Save disk space:** after an export is approved, offer to delete that video's `_work/` files.
   Use the `small` Whisper model unless the owner asks for better accuracy.
8. When the owner gives feedback ("captions too big", "cuts feel rushed"), turn it into a
   general rule and add it to the "Do / Don't" section of the style file used for that video.
9. Before saving to GitHub, run `git status` and confirm that no media files are staged.

## Tools
- **FFmpeg**: cutting, joining, audio mixing, loudness (-14 LUFS), final export.
- **Whisper** (via `faster-whisper`): run `python tools/transcribe.py <file>` to get word-level timestamps.
- **Remotion**: captions, titles and motion graphics written in code (`remotion/` folder).
- **HyperFrames**: HTML-based motion graphics, installed as a Claude Code plugin.
- **yt-dlp**: downloads reference videos into `references/<style>/`.

See `SETUP.md` for install details and test results.

## Shortcuts (skills)
| Type | What happens |
|---|---|
| `/setup-tools` | Install and test all 5 tools (run once per computer) |
| `/learn-style <style>` | Study reference videos and write `styles/<style>.md` |
| `/rough-cut [style]` | Transcribe the newest clip and propose a cut list (waits for approval) |
| `/render` | Apply approved cuts and style, run checks, export |
| `/save-workflow` | Save everything learned into the `my-reel-edit` skill |
| `/my-reel-edit` | (exists after `/save-workflow`) the whole edit in one go |

## Saving to GitHub
When the owner says "save to GitHub" (or at the end of a session), run:
`git add -A`, then check `git status` for media files, then `git commit -m "<short summary>"`
and `git push`. Explain what was saved in one sentence.
