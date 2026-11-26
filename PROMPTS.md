# The 5 prompts

**You don't need to copy these.** Each one is saved as a shortcut. In Claude Code, type the
`/command` in the left column. The full text is here in case you want to read or tweak it.
The detailed versions Claude actually follows are in `.claude/skills/<name>/SKILL.md`.

| Step | Type this | When |
|---|---|---|
| 1. Install | `/setup-tools` | Once per computer |
| 2. Style | `/learn-style <3-5 links>` | Once, then again whenever you want a new look |
| 3. First cut | `/rough-cut` | Every new video |
| 4. Render | `/render` | After you approve the cut |
| 5. Lock it in | `/save-workflow` | After your first 1-3 videos come out how you like |
| Everything at once | `/my-reel-edit` | After step 5 exists |

---

### 1. Install
```
Set up this folder as my video editing workspace. Install and test Remotion, HyperFrames, FFmpeg,
Whisper (word-level timestamps) and yt-dlp. Test each one: render a 3-second clip, transcribe 5
seconds of audio, download one short public video. Never modify originals; work on copies.
Document everything in SETUP.md.
```

### 2. Style (paste 3-5 links)
```
Download these into references/ with yt-dlp: [links]. Analyze them and write STYLE.md covering
pacing and cut frequency, caption font/size/position/words per line, color, zooms, graphics and
transitions, music and sound effects, and how the first 3 seconds hook. Cite the source video and
timestamp for each rule. Inspire, don't copy.
```

### 3. Initial cut (approval gate)
```
Transcribe the newest file in raw-footage with word-level timestamps. Propose a cut list
(source in/out, reason, confidence) for filler words, retakes (keep the best take, not the
latest), false starts and pauses over 0.4s. Cut on breaths or sentence ends, never mid-word.
Wait for my approval.
```

### 4. Render with style
```
Apply only the approved cuts with 2-4 frame audio crossfades. Then follow STYLE.md: captions,
graphics, music ducked under my voice, 9:16 1080x1920. Mix to -14 LUFS. QC for caption sync,
safe zones and audio pops. Show stills and the cut list, then export to exports/.
```

### 5. Lock it in
```
Save this workflow and STYLE.md as a skill called my-reel-edit. Add my corrections as Do/Don't rules.
```

---

## Giving feedback (the most important part)
After each render, describe what you'd change in plain words. Claude turns each note into a
permanent rule in STYLE.md. Examples:
- "The captions are too big and cover my face."
- "Cuts feel rushed, leave a tiny breath between sentences."
- "Music is too loud when I'm talking."
- "Start right on the first word, no intro."
- "Keep the part where I laugh, that's my personality."

## Saving your setup
Say **"save to GitHub"** at any point. Only text files are uploaded, never video.
