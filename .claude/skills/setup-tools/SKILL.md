---
name: setup-tools
description: Install and test the 5 video editing tools (FFmpeg, Whisper, Remotion, HyperFrames, yt-dlp) on this Windows computer and record results in SETUP.md. Use on a new computer or when a tool is missing or broken.
---

# Set up the video editing tools

The owner is not technical. Before each step, say in one sentence what you're doing.
Use PowerShell. Never touch `raw-footage/`.

## 0. Check where we are
- Confirm this folder is on the My Passport drive (`Get-Volume` shows the label). If it's on C:, warn
  the owner that video will fill up the laptop, and ask whether to continue.
- Check the free space on both C: and the drive, and report it in plain English.
- Create `_work/` and `models/` if they don't exist.

## 1. Base programs
Check what's already installed: `git --version`, `node --version` (needs 22 or newer for HyperFrames),
`python --version`, `ffmpeg -version`, `yt-dlp --version`.
For anything missing, run `tools/install-windows.ps1`. If a winget ID fails, run `winget search <name>`
and use the correct ID. After installing, tell the owner they may need to **close and reopen Claude Code**
so Windows can find the new programs, then pick up where you left off.

## 2. Whisper (word-level timestamps)
`python -m pip install --upgrade faster-whisper`
The model downloads into `models/` on the drive, not the laptop.

## 3. Remotion (graphics and captions in code)
If `remotion/` has no `package.json`, create a blank TypeScript project in `remotion/`
(`npx create-video@latest`, then pick the blank template. Follow the current prompts.)
If it already exists, run `npm install` inside it.
If Remotion has an official Claude Code agent skill, install that too. Check remotion.dev first.

## 4. HyperFrames (HTML motion graphics, by HeyGen)
Official source: github.com/heygen-com/hyperframes and hyperframes.heygen.com.
Install it as a Claude Code plugin:
```
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
```
If those commands have changed, follow the official quickstart. The plugin loads after Claude Code restarts.

## 5. Test every tool (each one must pass)
Put all test output in `_work/setup-test/`. Delete it at the end.
| Tool | Test |
|---|---|
| FFmpeg | Generate a 3-second 1080x1920 test video with a tone: `ffmpeg -f lavfi -i testsrc2=s=1080x1920:d=3 -f lavfi -i sine=d=3 -shortest _work/setup-test/ffmpeg.mp4` |
| Whisper | Run `python tools/transcribe.py <a file> --clip 5 --model base --out _work/setup-test/whisper`. If the owner has no clip yet, generate speech with Windows text-to-speech (System.Speech) to a WAV and transcribe that. Confirm it finds word timestamps |
| yt-dlp | Download one short public video at 720p max into `_work/setup-test/` (`-f "bv*[height<=720]+ba/b[height<=720]"`) |
| Remotion | Render a 3-second test composition to `_work/setup-test/remotion.mp4` |
| HyperFrames | Make a 3-second "Hello" title card and render it to `_work/setup-test/hyperframes.mp4` |

## 6. Record results
Update the **"Test results on this computer"** table in `SETUP.md`: tool, version, pass/fail, date, notes.
Write any fixes you needed into the "Problems & fixes" section so the next setup goes faster.
Then delete `_work/setup-test/`, save to GitHub (see CLAUDE.md), and tell the owner:
"All 5 tools work. Next: run /learn-style with 3-5 links to videos whose style you like."
