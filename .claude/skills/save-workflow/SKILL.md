---
name: save-workflow
description: Save the whole edit workflow plus everything learned from the owner's corrections into a reusable skill called my-reel-edit, so future videos need one command. Use once the owner likes a finished edit.
---

# Lock in the workflow

1. Read the style files in `styles/`, `CLAUDE.md` and the rough-cut and render skills, and remember the corrections the owner gave this session.
2. Make sure every correction is in the right style file under "Do / Don't" as a **general rule**
   (for example, "Captions never cover the face"), not a one-off note ("move caption at 0:12").
3. Create or update `.claude/skills/my-reel-edit/SKILL.md` with:
   - frontmatter: `name: my-reel-edit`, and a description saying it edits a new clip from raw-footage into a finished reel in the owner's style
   - the steps: pick the newest clip, transcribe, propose a cut list, **wait for approval**, pick the style (CLAUDE.md rule 6), render using that style file, QC, export, then capture feedback as rules
   - a short copy of the owner's most important Do/Don't rules for each style (the style files stay the main source)
   - a "Lessons learned" list of technical fixes from this session (for example, settings that fixed a sync issue)
4. Add a dated line to `CHANGELOG.md` (create it if missing) describing what changed.
5. Save to GitHub and tell the owner:
   "Saved. Next time, drop a clip in raw-footage and type /my-reel-edit."
