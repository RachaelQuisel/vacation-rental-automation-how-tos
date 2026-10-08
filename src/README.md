# Build code

This folder has the code that builds the videos in this repo.

| File | What it does |
|---|---|
| [v1.html](v1.html) | Scene for "Schedule your cleaners by text": painted SVG background, phone screens, steps, and the `render(t)` timing function. Open it in Chrome to see frame 0. Add `?sq` for the square layout. |
| [v2.html](v2.html) | Scene for "Monthly TOT and TBID tax prep". |
| [v3.html](v3.html) | Scene for "When your cleaner can't make it, the next one is asked automatically". |
| [v6.html](v6.html) | Scene for "Door codes for every guest, assigned and revoked automatically". The door codes in it are invented sample codes. |
| [v5.html](v5.html) | Scene for "When an inspection finds a problem, the right contractor is scheduled automatically". |
| [render-v5.sh](render-v5.sh) | Same steps as the other render scripts, for v5. Output goes to `out-v5/`. |
| [v7.html](v7.html) | Scene for "A morning briefing in Slack so your whole team starts the day on the same page" (Ops Today). |
| [render-v7.sh](render-v7.sh) | Same steps as the other render scripts, for v7. Output goes to `out-v7/`. |
| [cap.js](cap.js) | Opens a scene in headless Chrome and saves one PNG per frame. |
| [render-v1.sh](render-v1.sh), [render-v2.sh](render-v2.sh), [render-v3.sh](render-v3.sh), [render-v6.sh](render-v6.sh) | Each one captures wide and square frames, encodes both loops, copies the posters, pulls QC frames, and prints a format check. Output goes to `out/`, `out-v2/`, `out-v3/`, and `out-v6/`. |
| [make-music-version.sh](make-music-version.sh) | Plays the wide loop twice and adds a leveled 20 second music excerpt. |
| [package.json](package.json) | Pins `playwright-core`. |
| [package-lock.json](package-lock.json) | Locks the exact `playwright-core` download, so `npm ci` installs the same version. |
| [fonts/](fonts/) | The font files the scenes use (Nunito, Caveat, DejaVu Sans Mono, and DejaVu Sans for symbols), their licenses, and a `fonts.conf` that makes Chrome use only these files. |

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

# Silent loops, posters, and QC frames. Output goes to src/out/ (v1), src/out-v2/, src/out-v3/, or src/out-v6/.
./render-v1.sh
./render-v2.sh
./render-v3.sh
./render-v6.sh

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
| v6 | ["Parisian" by Kevin MacLeod](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1100120) | 0.15 |
| v5 | ["Valse Gymnopedie" by Kevin MacLeod](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN2100012) | 14.05 |
| v7 | ["Suave Standpipe" by Kevin MacLeod](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1500078) | 86.39 |

```bash
./make-music-version.sh out/loop-1920x1080.mp4    path/to/le-croissant.mp3       76.95 out/schedule-cleaners-by-text.mp4
./make-music-version.sh out-v2/loop-1920x1080.mp4 path/to/la-pompe-du-trompe.mp3 87.42 out-v2/monthly-tax-prep.mp4
./make-music-version.sh out-v3/loop-1920x1080.mp4 path/to/rendezvous.mp3         99.12 out-v3/backup-cleaner-coverage.mp4
./make-music-version.sh out-v6/loop-1920x1080.mp4 path/to/parisian.mp3           0.15 out-v6/guest-door-codes.mp4
./make-music-version.sh out-v5/loop-1920x1080.mp4 path/to/valse-gymnopedie.mp3   14.05 out-v5/property-inspection.mp4
./make-music-version.sh out-v7/loop-1920x1080.mp4 path/to/suave-standpipe.mp3    86.39 out-v7/ops-today.mp4
```

The v1 to v3 tracks are by Shane Ivers ([silvermansound.com](https://www.silvermansound.com)) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The v6 track is by Kevin MacLeod ([incompetech.com](https://incompetech.com)), also under CC BY 4.0. The v5 track is also by Kevin MacLeod, under CC BY 4.0. So is the v7 track. The exact credit for each is in its video folder README. Keep it with the music version wherever you share it.

## Notes

- The `out/` folders and `node_modules/` are ignored by git.
- `render(t)` sets every element from `t` alone, so frames can be captured in any order and should come out the same each run. In a check on Oct 7, 2026, v1 and v2 rebuilt byte for byte. The v3 square loop differed by tiny anti-aliasing changes.
- Results can differ slightly with other Chrome or ffmpeg versions, or with other font files.
- A later dry run on a fresh clone, on Oct 7, 2026, rebuilt every silent loop and poster for all four videos byte for byte, including the v3 square loop. See "Rebuild from scratch" below.

## Rebuild from scratch

These steps start from a fresh clone and end with every finished file in `videos/`. They were tested on Oct 7, 2026, on a fresh clone of `main`.

### Tools and versions

| Tool | Version used | Notes |
|---|---|---|
| Operating system | Debian GNU/Linux 13, x86_64 | Any Linux or macOS with the tools below should work. Windows was not tested. |
| Node.js and npm | Node 20.19.2, npm 9.2.0 | Node 20 or newer. |
| `playwright-core` | 1.63.0 | Installed by `npm ci` from `package-lock.json`. It does not download a browser. |
| Google Chrome | 154.0.8037.57 | Or Chromium. Set `CHROME_PATH` if it is not at `/usr/bin/google-chrome`. |
| ffmpeg and ffprobe | 7.1.5 (Debian build), with `libx264` and the built-in AAC encoder | |
| fontconfig | 2.15.0 | Linux only. Chrome uses it to find fonts, and `fc-cache` uses it to register them. |
| Python 3 | 3.13.5 | Only for `make-music-version.sh`. Standard library only. |
| curl | any | To download the music. |

Other versions should work, but the output may not be byte for byte the same.

### Fonts

The scenes use three fonts: Nunito (all interface and headline text), Caveat (the handwritten note), and DejaVu Sans Mono (the door code keypad and codes in v6). Chrome also uses DejaVu Sans, regular and bold, for symbols that Nunito doesn't have, such as ✓ and ●, so it is bundled too. The files are in [fonts/](fonts/), with their licenses: [OFL-Nunito.txt](fonts/OFL-Nunito.txt), [OFL-Caveat.txt](fonts/OFL-Caveat.txt), and [LICENSE-DejaVu.txt](fonts/LICENSE-DejaVu.txt). Download pages: [Nunito](https://fonts.google.com/specimen/Nunito), [Caveat](https://fonts.google.com/specimen/Caveat), [DejaVu](https://dejavu-fonts.github.io/).

Pick one of these:

- **Install them as system or user fonts (recommended).** On Linux, copy the `.ttf` files to `~/.local/share/fonts/` and run `fc-cache -f`. On macOS, open each `.ttf` file and click Install Font. The original build and the byte-for-byte dry runs below used system-installed copies of these same font files.
- **Use the bundled fonts without installing them (Linux).** Put `FONTCONFIG_FILE="$PWD/fonts/fonts.conf"` in front of each render command, run from `src/`. Chrome then sees only the files in `fonts/`. In a full test on Oct 7, 2026, this gave videos that look the same, but not byte for byte: the text anti-aliasing and spacing differed slightly. Use it when you can't install fonts and a close match is enough.

If a font is missing, Chrome falls back to another font and the layout will not match.

### Steps

```bash
git clone https://github.com/RachaelQuisel/vacation-rental-automation-how-tos.git
cd vacation-rental-automation-how-tos/src
npm ci

# Install the fonts first (see Fonts above). On Linux:
mkdir -p ~/.local/share/fonts && cp fonts/*.ttf ~/.local/share/fonts/ && fc-cache -f

# 1. Silent loops, posters, and QC frames. About 3.5 to 4.5 minutes each on the test machine.
./render-v1.sh     # output in out/
./render-v2.sh     # output in out-v2/
./render-v3.sh     # output in out-v3/
./render-v6.sh     # output in out-v6/
./render-v5.sh     # output in out-v5/
./render-v7.sh     # output in out-v7/

# 2. Download the music. The audio files are not in this repo (see the table below).
mkdir -p music
curl -L -o music/le-croissant.mp3       https://www.silvermansound.com/wp-content/uploads/le-croissant.mp3
curl -L -o music/la-pompe-du-trompe.mp3 https://www.silvermansound.com/wp-content/uploads/la-pompe-du-trompe.mp3
curl -L -o music/rendezvous.mp3         https://www.silvermansound.com/wp-content/uploads/rendezvous.mp3
curl -L -o music/parisian.mp3           https://incompetech.com/music/royalty-free/mp3-royaltyfree/Parisian.mp3
curl -L -o music/valse-gymnopedie.mp3   "https://incompetech.com/music/royalty-free/mp3-royaltyfree/Valse%20Gymnopedie.mp3"
curl -L -o music/suave-standpipe.mp3    "https://incompetech.com/music/royalty-free/mp3-royaltyfree/Suave%20Standpipe.mp3"
sha256sum music/*.mp3    # compare with the table below (on macOS: shasum -a 256 music/*.mp3)

# 3. Music versions: the wide loop played twice, with a leveled 20 second excerpt.
./make-music-version.sh out/loop-1920x1080.mp4    music/le-croissant.mp3       76.95 out/schedule-cleaners-by-text.mp4
./make-music-version.sh out-v2/loop-1920x1080.mp4 music/la-pompe-du-trompe.mp3 87.42 out-v2/monthly-tax-prep.mp4
./make-music-version.sh out-v3/loop-1920x1080.mp4 music/rendezvous.mp3         99.12 out-v3/backup-cleaner-coverage.mp4
./make-music-version.sh out-v6/loop-1920x1080.mp4 music/parisian.mp3           0.15  out-v6/guest-door-codes.mp4
./make-music-version.sh out-v5/loop-1920x1080.mp4 music/valse-gymnopedie.mp3   14.05 out-v5/property-inspection.mp4
./make-music-version.sh out-v7/loop-1920x1080.mp4 music/suave-standpipe.mp3    86.39 out-v7/ops-today.mp4

# 4. Compare with the committed files. "cmp" prints nothing when two files are the same.
cmp out/loop-1920x1080.mp4    ../videos/schedule-cleaners-by-text/loop-1920x1080.mp4
cmp out-v2/loop-1920x1080.mp4 ../videos/monthly-tax-prep/loop-1920x1080.mp4
cmp out-v3/loop-1920x1080.mp4 ../videos/backup-cleaner-coverage/loop-1920x1080.mp4
cmp out-v6/loop-1920x1080.mp4 ../videos/guest-door-codes/loop-1920x1080.mp4
cmp out-v5/loop-1920x1080.mp4 ../videos/property-inspection/loop-1920x1080.mp4
cmp out-v7/loop-1920x1080.mp4 ../videos/ops-today/loop-1920x1080.mp4
```

`src/music/` is in `.gitignore`, so the audio files are not committed by accident.

Music downloads, checked on Oct 7, 2026. Each file matched the one used for the original build.

| Video | Track | Source page | Direct download | SHA-256 |
|---|---|---|---|---|
| v1 | "Le Croissant" by Shane Ivers | [silvermansound.com](https://www.silvermansound.com/free-music/le-croissant) | `https://www.silvermansound.com/wp-content/uploads/le-croissant.mp3` | `aa397311ae84a5382419106d26a9c9c673a90c8c27eea8db21bb9747ccbe84f5` |
| v2 | "La Pompe Du Trompe" by Shane Ivers | [silvermansound.com](https://www.silvermansound.com/free-music/la-pompe-du-trompe) | `https://www.silvermansound.com/wp-content/uploads/la-pompe-du-trompe.mp3` | `78641efe3f097a43987645d70b4d7bc3a424c80aa3790278a4abd73d6b378b54` |
| v3 | "Rendezvous" by Shane Ivers | [silvermansound.com](https://www.silvermansound.com/free-music/rendezvous) | `https://www.silvermansound.com/wp-content/uploads/rendezvous.mp3` | `0a22eaf1586a23ff7d7a2264d1d0887eb64c997c02cc9f198940c8e8fce7724c` |
| v6 | "Parisian" by Kevin MacLeod | [incompetech.com](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1100120) | `https://incompetech.com/music/royalty-free/mp3-royaltyfree/Parisian.mp3` | `b8098a3b4fa1b58df46b280d6e4e6e8c847301a26d69a6cec8111b7338a020ec` |
| v5 | "Valse Gymnopedie" by Kevin MacLeod | [incompetech.com](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN2100012) | `https://incompetech.com/music/royalty-free/mp3-royaltyfree/Valse%20Gymnopedie.mp3` | `64acef868e26a9f4d9559c6ddee5e8e4c0890865a186069b49d30b99e6e81684` |
| v7 | "Suave Standpipe" by Kevin MacLeod | [incompetech.com](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1500078) | `https://incompetech.com/music/royalty-free/mp3-royaltyfree/Suave%20Standpipe.mp3` | `14713f9649ecf4883763d482be64dc730cfb3af06c580ef631c54aca3fac62b3` |

If a direct download link stops working, download the track from its source page instead.

### Where each output goes

| Build output | Committed file |
|---|---|
| `out/loop-1920x1080.mp4`, `out/loop-1080x1080.mp4`, `out/poster.png`, `out/poster-square.png` | Same names in `videos/schedule-cleaners-by-text/` |
| `out/schedule-cleaners-by-text.mp4` | `videos/schedule-cleaners-by-text/schedule-cleaners-by-text.mp4` |
| `out-v2/` files, and `out-v2/monthly-tax-prep.mp4` | Same names in `videos/monthly-tax-prep/` |
| `out-v3/` files, and `out-v3/backup-cleaner-coverage.mp4` | Same names in `videos/backup-cleaner-coverage/` |
| `out-v6/` files, and `out-v6/guest-door-codes.mp4` | Same names in `videos/guest-door-codes/` |
| `out-v5/` files, and `out-v5/property-inspection.mp4` | Same names in `videos/property-inspection/` |
| `out-v7/` files, and `out-v7/ops-today.mp4` | Same names in `videos/ops-today/` |

The `qc/` frames and the `frames-*` folders are for checking by eye and are not committed.

### Dry-run results (Oct 7, 2026)

Fresh clone of `main` at 083f587, with the tool versions above:

| Video | Silent loops and posters | Music version |
|---|---|---|
| v1 Schedule your cleaners by text | Byte for byte the same | A close match, not byte for byte. The committed file was made with an earlier form of the same steps (see the v1 post-run analysis). Its loudness is about -16.5 LUFS, and the script's output is about -16.1 LUFS. |
| v2 Monthly TOT and TBID tax prep | Byte for byte the same | Byte for byte the same |
| v3 Backup cleaner | Byte for byte the same | Byte for byte the same |
| v6 Door codes | Byte for byte the same | Byte for byte the same |
| v5 Property inspection | Byte for byte the same (rebuilt with `render-v5.sh` from this repo, compared with the final render) | Byte for byte the same |
| v7 Ops Today | Byte for byte the same (rebuilt with `render-v7.sh` from this repo, compared with the final render) | Byte for byte the same |

All of these runs used system-installed fonts. A full run with only the bundled fonts (`fonts.conf`) looked the same but was not byte for byte the same.

