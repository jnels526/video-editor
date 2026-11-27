# Styles

Each file here is one editing style. Claude picks one for every edit.

| File | Used for |
|---|---|
| `history.md` | History storytelling: talking to camera with archival photos and maps |
| `gym.md` | Gym: women doing hard things, plus tips to succeed |
| `travel.md` | Travel and faceless videos |
| `storytelling.md` | Storytelling rules used for **every** video (hooks, tension, payoff) |
| `_template.md` | Blank starting point for a new style |

## How Claude picks the style
1. If you name it ("edit this as **gym**", `/rough-cut gym`), Claude uses that one.
2. Otherwise, if the clip is in a style's subfolder (`raw-footage/gym/`, `raw-footage/travel/`, `raw-footage/history/`), Claude uses that style.
3. Otherwise Claude asks you which one to use.

Reference videos for each style live in `references/<style>/`. (The history references are the `reference1-10.mp4` files directly in `references/`.)

## Adding a new style
Type `/learn-style <new name> <3-5 links>`, for example `/learn-style cooking https://...`.
Claude copies `_template.md` to `styles/cooking.md`, saves the references in `references/cooking/` and fills in the file.
