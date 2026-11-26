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
| FFmpeg | | 3-second 1080x1920 test video | | | |
| Whisper | | Transcribe 5 seconds of audio with word timestamps | | | |
| yt-dlp | | Download one short public video | | | |
| Remotion | | Render a 3-second composition | | | |
| HyperFrames | | Render a 3-second title card | | | |

## Problems & fixes
*Claude adds anything that went wrong during setup, and how it was fixed, so the next setup is faster.*

- (none yet)

## Setting up on another computer
1. Plug in My Passport (the folder is already on it), **or** download the setup from GitHub again (see README step 3).
2. Open Claude Code in the folder and type `/setup-tools`.
