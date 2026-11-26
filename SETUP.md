# Setup

> You don't need to do any of this by hand. Type **`/setup-tools`** in Claude Code and it
> installs, tests and fills in the results table below. This page is the record of what's installed.

## The 5 tools
| Tool | What it does in this workflow | How it's installed (Windows) |
|---|---|---|
| **FFmpeg** | Cuts, joins, mixes audio, sets loudness, exports | `winget install Gyan.FFmpeg` |
| **Whisper** (faster-whisper) | Word-by-word transcript with timestamps, used for cuts and captions | `python -m pip install faster-whisper` |
| **Remotion** | Captions, titles, zooms and graphics, written as code | `npx create-video@latest` in `remotion/` |
| **HyperFrames** (HeyGen) | HTML-based animated graphics and title cards | Claude Code plugin: `claude plugin marketplace add heygen-com/hyperframes` then `claude plugin install hyperframes@hyperframes` |
| **yt-dlp** | Downloads reference videos to study | `winget install yt-dlp.yt-dlp` |

Supporting programs: **Git** (saves to GitHub), **Node.js 22+** (runs Remotion and HyperFrames),
**Python 3.12** (runs Whisper). `tools/install-windows.ps1` installs all of the base programs at once.

## Where things live (saving laptop space)
- **Laptop (C:)**: only the installed programs (around 1-2 GB in total).
- **My Passport drive**: this whole folder, including footage, references, music, exports, Whisper models and Remotion's `node_modules`.
- **GitHub**: only the text files (instructions, style guide, scripts, Remotion code). Video never goes to GitHub.

Whisper model sizes (downloaded once to `models/` on the drive):
`base` ≈ 150 MB (quick, OK accuracy) · `small` ≈ 500 MB (**default**, good) · `medium` ≈ 1.5 GB (best for a laptop, slow).

## Test results on this computer
*Filled in by `/setup-tools`.*

| Tool | Version | Test | Result | Date | Notes |
|---|---|---|---|---|---|
| FFmpeg | 9.1 (gyan.dev full build) | 3-second 1080x1920 test video | Pass | 2026-11-26 | Video + audio, 3.0 s |
| Whisper | faster-whisper 1.2.1 (Python 3.12.10, PyAV 18.1.1) | Transcribe 5 seconds of audio with word timestamps | Pass | 2026-11-26 | Windows text-to-speech clip, `base` model, 12 words with timestamps |
| yt-dlp | 2026.11.23 | Download one short public video | Pass | 2026-11-26 | 720p max, merged with FFmpeg |
| Remotion | 4.0.547 (Node 26.13.1) | Render a 3-second composition | Pass | 2026-11-26 | `SetupTest` composition, 1080x1920. Official Remotion agent skills installed in `remotion/.claude/skills` |
| HyperFrames | 0.9.99 (Claude Code plugin) | Render a 3-second title card | Pass | 2026-11-26 | "Hello" card, 1080x1920, rendered in ~32 s |

Other programs: Git 2.56.1, Node.js 26.13.1, npm 11.20.0, Python 3.12.10.

## Problems & fixes
*Claude adds anything that went wrong during setup, and how it was fixed, so the next setup is faster.*

- **Whisper crashed with `TypeError: open() got an unexpected keyword argument 'metadata_errors'`.**
  The newest PyAV (19.x) doesn't work with faster-whisper 1.2.1. Fix: `python -m pip install "av<19"`.
- **New programs not found right after install.** Instead of restarting Claude Code, reload PATH in the same
  PowerShell window: `$env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User')`
- **`claude` command not on PATH.** It lives at `%USERPROFILE%\.local\bin\claude.exe`; call it by full path for the plugin commands.
- **Remotion without prompts:** `npx create-video@latest --yes --blank --skills remotion` creates the project and installs the official agent skills in one go.
  The skills (in `remotion/.agents/`) are kept out of GitHub because they include icon images; on a new
  computer, ask Claude to reinstall the Remotion agent skills listed in `remotion/skills-lock.json`.
- **HyperFrames renders from the command line** with the plugin's bundled CLI:
  `node <plugin folder>\skills\hyperframes\scripts\plugin-cli.mjs render --quality draft -o out.mp4`
  (plugin folder: `%USERPROFILE%\.claude\plugins\cache\hyperframes\hyperframes\<version>`).

## Setting up on another computer
1. Plug in My Passport (the folder is already on it), **or** download the setup from GitHub again (see README step 3).
2. Open Claude Code in the folder and type `/setup-tools`.
