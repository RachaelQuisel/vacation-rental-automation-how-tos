# Build code

This folder has the code that builds the videos in this repo.

| File | What it does |
|---|---|
| [v1.html](v1.html) | Scene for "Schedule your cleaners by text": painted SVG background, phone screens, steps, and the `render(t)` timing function. Open it in Chrome to see frame 0. Add `?sq` for the square layout. |
| [v2.html](v2.html) | Scene for "Monthly TOT and TBID tax prep". |
| [v3.html](v3.html) | Scene for "When your cleaner can't make it, the next one is asked automatically". |
| [cap.js](cap.js) | Opens a scene in headless Chrome and saves one PNG per frame. |
| [render-v1.sh](render-v1.sh), [render-v2.sh](render-v2.sh), [render-v3.sh](render-v3.sh) | Each one captures wide and square frames, encodes both loops, copies the posters, pulls QC frames, and prints a format check. Output goes to `out/`, `out-v2/`, and `out-v3/`. |
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

# Silent loops, posters, and QC frames. Output goes to src/out/ (v1), src/out-v2/, or src/out-v3/.
./render-v1.sh
./render-v2.sh
./render-v3.sh

# Quick test with only 0.5 seconds of frames.
DUR=0.5 OUT=out-test ./render-v1.sh
```

Each full capture took about 2 to 4 minutes on the build machine.

For the music versions, download each track from its source page. The audio files are not in this repo.

| Video | Track and source page | Excerpt start (s) |
|---|---|---|
| v1 | ["Le Croissant"](https://www.silvermansound.com/free-music/le-croissant) | 76.95 |
| v2 | ["La Pompe Du Trompe"](https://www.silvermansound.com/free-music/la-pompe-du-trompe) | 87.42 |
| v3 | ["Rendezvous"](https://www.silvermansound.com/free-music/rendezvous) | 99.12 |

```bash
./make-music-version.sh out/loop-1920x1080.mp4    path/to/le-croissant.mp3       76.95 out/schedule-cleaners-by-text.mp4
./make-music-version.sh out-v2/loop-1920x1080.mp4 path/to/la-pompe-du-trompe.mp3 87.42 out-v2/monthly-tax-prep.mp4
./make-music-version.sh out-v3/loop-1920x1080.mp4 path/to/rendezvous.mp3         99.12 out-v3/backup-cleaner-coverage.mp4
```

All three tracks are by Shane Ivers ([silvermansound.com](https://www.silvermansound.com)) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The exact credit line for each is in its video folder README. Keep it with the music version wherever you share it.

## Notes

- The `out/` folders and `node_modules/` are ignored by git.
- `render(t)` sets every element from `t` alone, so frames can be captured in any order and should come out the same each run. In a check on Oct 7, 2026, v1 and v2 rebuilt byte for byte. The v3 square loop differed by tiny anti-aliasing changes.
- Results can differ slightly with other Chrome or ffmpeg versions, or with other font files.
