# Build code

This folder has the code that builds the "Schedule your cleaners by text" video.

| File | What it does |
|---|---|
| [v1.html](v1.html) | The scene: painted SVG background, phone screens, steps, and the `render(t)` timing function. Open it in Chrome to see frame 0. Add `?sq` for the square layout. |
| [cap.js](cap.js) | Opens a scene in headless Chrome and saves one PNG per frame. |
| [render-v1.sh](render-v1.sh) | Captures wide and square frames, encodes both loops, copies the posters, pulls QC frames, and prints a format check. |
| [make-music-version.sh](make-music-version.sh) | Plays the wide loop twice and adds a leveled 20 second music excerpt. |
| [package.json](package.json) | Pins `playwright-core`. |

## What you need

- Node.js 20 or newer and npm.
- Google Chrome or Chromium. The build used Chrome 154. Set `CHROME_PATH` if it is not at `/usr/bin/google-chrome`.
- `playwright-core` 1.63.0 (installed by `npm install`). It is a library that controls a browser from a script.
- ffmpeg and ffprobe with `libx264` and AAC. The build used ffmpeg 7.1.5.
- Python 3 (only for the music script, to read ffmpeg's JSON output).
- The fonts [Nunito](https://fonts.google.com/specimen/Nunito) and [Caveat](https://fonts.google.com/specimen/Caveat), installed as system fonts. The page does not download them. If they are missing, Chrome falls back to other fonts and the layout will not match.

## Run it

```bash
cd src
npm install

# Silent loops, posters, and QC frames. Output goes to src/out/.
./render-v1.sh

# Quick test with only 0.5 seconds of frames.
DUR=0.5 OUT=out-test ./render-v1.sh
```

Each full capture took about 2 to 4 minutes on the build machine.

For the music version, download "Le Croissant" by Shane Ivers from its [source page](https://www.silvermansound.com/free-music/le-croissant). The audio file is not in this repo. Then run:

```bash
./make-music-version.sh out/loop-1920x1080.mp4 path/to/le-croissant.mp3 76.95 out/schedule-cleaners-by-text.mp4
```

Music: "Le Croissant" by Shane Ivers ([silvermansound.com](https://www.silvermansound.com)), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Keep this credit with the music version wherever you share it.

## Notes

- The `out/` folders and `node_modules/` are ignored by git.
- `render(t)` sets every element from `t` alone, so frames can be captured in any order and should come out the same each run.
- Results can differ slightly with other Chrome or ffmpeg versions, or with other font files.
