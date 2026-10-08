# Door codes for every guest, assigned and revoked automatically

A guest books and gets their own door code, sent in the welcome message, a week before, and a day before their stay. Every guest and contractor has a unique code, and each code is revoked after checkout and never reused.

Uses sample data. The names, dates, and door codes in the video are made up.

## Files

| File | What it is |
|---|---|
| [guest-door-codes.mp4](guest-door-codes.mp4) | The main how-to video. 1920x1080, 20 seconds, with music. |
| [loop-1920x1080.mp4](loop-1920x1080.mp4) | Silent 10 second loop, wide. Made for a website. |
| [loop-1080x1080.mp4](loop-1080x1080.mp4) | Silent 10 second loop, square. Made for phones and social posts. |
| [poster.png](poster.png) | Still frame for the wide video (8.8 seconds in). |
| [poster-square.png](poster-square.png) | Still frame for the square video (8.8 seconds in). |
| [script.md](script.md) | On-screen script and storyboard, beat by beat. |
| [post-run-analysis.md](post-run-analysis.md) | How this video was built, checked, and fixed, plus open items. |
| [field-guide.md](field-guide.md) | Every label on screen, how each person sees the system, and a short FAQ. |

## Music credit

The music is in `guest-door-codes.mp4` only. The two loops are silent.

```
"Parisian" Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 4.0
http://creativecommons.org/licenses/by/4.0/
```

Links: [incompetech.com](https://incompetech.com), [track page](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1100120), [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/)

The track was cut to a 20 second excerpt, faded in and out, and leveled for loudness. If you share this video, please keep this credit with it.

## How it was made

See [How these videos are made](../../docs/how-to-make-these-videos.md) and the build code in [src/](../../src/) (`v6.html` and `render-v6.sh`).

## Rebuild from scratch

Full prerequisites, tool versions, and font setup are in [src/README.md](../../src/README.md#rebuild-from-scratch). For this video only:

```bash
git clone https://github.com/RachaelQuisel/vacation-rental-automation-how-tos.git
cd vacation-rental-automation-how-tos/src
npm ci
export FONTCONFIG_FILE="$PWD/fonts/fonts.conf"   # optional, Linux: use only the bundled fonts

# Silent loops, posters (frame 264 (8.8 seconds)), and QC frames, in src/out-v6/
./render-v6.sh

# Music version. The audio file is not in this repo, so download it first.
mkdir -p music
curl -L -o music/parisian.mp3 https://incompetech.com/music/royalty-free/mp3-royaltyfree/Parisian.mp3
./make-music-version.sh out-v6/loop-1920x1080.mp4 music/parisian.mp3 0.15 out-v6/guest-door-codes.mp4

# Compare with the committed files. cmp prints nothing when they match.
for f in loop-1920x1080.mp4 loop-1080x1080.mp4 poster.png poster-square.png guest-door-codes.mp4; do cmp out-v6/$f ../videos/guest-door-codes/$f; done
```

In a dry run on a fresh clone on Oct 7, 2026: The silent loops, posters, and music version all rebuilt byte for byte.

## Rebuild checklist

| Item | Where it is |
|---|---|
| 1. Source files and art | [src/v6.html](../../src/v6.html). The painted background, screens, and text are all drawn in code in this one file, so there are no separate image files. Fonts are in [src/fonts/](../../src/fonts/), with download links in [src/README.md](../../src/README.md#fonts). |
| 2. Build scripts, tools, and versions | [src/render-v6.sh](../../src/render-v6.sh), [src/cap.js](../../src/cap.js), [src/make-music-version.sh](../../src/make-music-version.sh), [src/package.json](../../src/package.json), [src/package-lock.json](../../src/package-lock.json). Tool versions are in [src/README.md](../../src/README.md#tools-and-versions). |
| 3. Inputs: script and storyboard | [script.md](script.md). The sample data is written into [src/v6.html](../../src/v6.html). |
| 4. Step-by-step rebuild | "Rebuild from scratch" above, and [src/README.md](../../src/README.md#rebuild-from-scratch) |
| 5. Design rules | [docs/design-schema.md](../../docs/design-schema.md) and [docs/how-to-make-these-videos.md](../../docs/how-to-make-these-videos.md) |
| 6. Music credit and source | "Music credit" above. Source page: ["Parisian" by Kevin MacLeod](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1100120). The audio file is not in this repo. |
| 7. Finished outputs | The two loops, two posters, and `guest-door-codes.mp4` in this folder |
| 8. Where it was shared | Below |

## Where it was shared

Not shared yet as of Oct 7, 2026.
