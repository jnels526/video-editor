# AI Video Editor

Edit short videos (Reels, TikToks, Shorts) by talking to Claude. Drop in a clip, approve a cut list,
get a finished, captioned 9:16 video in your own style.

**Where things live**
- 🎞️ **My Passport drive**: this folder, plus all video, music and exports
- 💻 **Laptop**: only the installed programs
- ☁️ **GitHub**: only the instructions and style guide (text), as a backup. Video never uploads.

---

## One-time setup (about 30-45 minutes, mostly waiting)

### 1. Install Claude Code
Install Claude Code for Windows using the instructions at **claude.com/claude-code**
(the desktop app is easiest), and sign in.

### 2. Install GitHub Desktop
Download **desktop.github.com**, install it, and sign in with your GitHub account.
This lets you copy your setup onto the drive without typing Git commands.

### 3. Put the setup on your My Passport drive
1. Plug in My Passport.
2. In GitHub Desktop: **File → Clone repository → `video-editor`**.
3. For **Local path**, click **Choose…** and select the **My Passport** drive (for example `E:\`).
4. Click **Clone**. You now have an `video-editor` folder on the drive.

### 4. Open it in Claude Code
Open Claude Code and choose the `video-editor` folder on My Passport as the project folder.

### 5. Install the tools
Type:
```
/setup-tools
```
Claude installs and tests FFmpeg, Whisper, Remotion, HyperFrames and yt-dlp. Click **allow**
when it asks permission to run things. If it asks you to restart Claude Code, do that, then say "continue".

### 6. Teach it your style
Find 3-5 short videos whose editing you love, then type the style name and the links:
```
/learn-style gym https://link1 https://link2 https://link3
```
You can have as many styles as you like (history, gym, travel...). See `styles/README.md`.
Read the summary and tell Claude anything that's off.

### 7. (Optional) Add music and fonts
Put music tracks, sound effects, logos or fonts you're allowed to use into the `assets` folder.

---

## Editing a video (every time)

1. **Copy your clip** into the `raw-footage` folder on My Passport. Short clips (30-90 seconds) work best at first.
   Tip: put it in `raw-footage\gym`, `raw-footage\travel`, `raw-footage\history` or `raw-footage\brand` and Claude picks that style automatically.
2. Type **`/rough-cut`** (or `/rough-cut gym` to choose the style yourself). Claude transcribes the clip and shows a list of proposed cuts.
   Reply **"approved"**, or say what to change, for example "keep #3" or "cut the part about my cat".
3. Type **`/render`**. Claude adds captions, zooms, graphics and music in your style, checks the result,
   and saves it to the `exports` folder.
4. **Watch it, then say what to change** in plain words. Claude fixes it *and* remembers the rule for next time.
5. After your first 1-3 good videos, type **`/save-workflow`**. From then on, you only need:
   ```
   /my-reel-edit
   ```

## Saving your setup to GitHub
Just tell Claude **"save to GitHub"**. (Or in GitHub Desktop: write a short summary → **Commit** → **Push origin**.)
Only text files upload. Video is blocked automatically.

## Keeping your laptop free
- Everything big stays on My Passport. **Plug the drive in before you start Claude Code.**
- After you're happy with an export, Claude offers to delete the scratch files in `_work`. Say yes.
- Move finished videos off the drive when you've posted them.

## What's in this folder
| | |
|---|---|
| `raw-footage/` | Your original clips. Claude never changes these. |
| `references/` | Videos you like, one folder per style, used to learn each style |
| `assets/` | Music, sound effects, fonts, logos |
| `exports/` | Finished videos (`name - v1.mp4`, `v2`…) |
| `styles/` | Your style guides (history, gym, travel, brand). Each grows with every bit of feedback |
| `PROMPTS.md` | The 5 commands and the full prompts behind them |
| `SETUP.md` | What's installed, and test results |
| `CLAUDE.md` | Rules Claude always follows in this folder |
| `tools/` | Helper scripts (transcription, Windows installer) |
| `.claude/skills/` | The `/commands` |

## If something goes wrong
Tell Claude what happened in plain words ("the captions are out of sync", "it says ffmpeg not found").
For tool problems, run `/setup-tools` again. It re-tests everything and fixes what's missing.
