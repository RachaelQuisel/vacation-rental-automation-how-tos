# When your cleaner can't make it, the next one is asked automatically

Each booking creates a cleaning task and a calendar invite. If a cleaner declines, it goes to the next one, and you get a text if a day still needs coverage.

Uses sample data. The names, dates, and messages in the video are made up.

## Files

| File | What it is |
|---|---|
| [backup-cleaner-coverage.mp4](backup-cleaner-coverage.mp4) | The main how-to video. 1920x1080, 20 seconds, with music. |
| [loop-1920x1080.mp4](loop-1920x1080.mp4) | Silent 10 second loop, wide. Made for a website. |
| [loop-1080x1080.mp4](loop-1080x1080.mp4) | Silent 10 second loop, square. Made for phones and social posts. |
| [poster.png](poster.png) | Still frame for the wide video (8.8 seconds in). |
| [poster-square.png](poster-square.png) | Still frame for the square video (8.8 seconds in). |
| [script.md](script.md) | On-screen script and storyboard, beat by beat. |
| [post-run-analysis.md](post-run-analysis.md) | How this video was built, checked, and fixed, plus open items. |
| [field-guide.md](field-guide.md) | Every label on screen, how each person sees the system, and a short FAQ. |

## Music credit

The music is in `backup-cleaner-coverage.mp4` only. The two loops are silent.

Music: "Rendezvous" by Shane Ivers ([silvermansound.com](https://www.silvermansound.com)), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

The track was cut to a 20 second excerpt, faded in and out, and leveled for loudness. If you share this video, please keep this credit line with it.

## How it was made

See [How these videos are made](../../docs/how-to-make-these-videos.md) and the build code in [src/](../../src/) (`v3.html` and `render-v3.sh`).

## Rebuild from scratch

Full prerequisites, tool versions, and font setup are in [src/README.md](../../src/README.md#rebuild-from-scratch). For this video only:

```bash
git clone https://github.com/RachaelQuisel/vacation-rental-automation-how-tos.git
cd vacation-rental-automation-how-tos/src
npm ci
mkdir -p ~/.local/share/fonts && cp fonts/*.ttf ~/.local/share/fonts/ && fc-cache -f   # Linux: install the fonts (macOS: see src/README.md)

# Silent loops, posters (frame 264, 8.8 seconds), and QC frames, in src/out-v3/
./render-v3.sh

# Music version. The audio file is not in this repo, so download it first.
mkdir -p music
curl -L -o music/rendezvous.mp3 https://www.silvermansound.com/wp-content/uploads/rendezvous.mp3
./make-music-version.sh out-v3/loop-1920x1080.mp4 music/rendezvous.mp3 99.12 out-v3/backup-cleaner-coverage.mp4

# Compare with the committed files. cmp prints nothing when they match.
for f in loop-1920x1080.mp4 loop-1080x1080.mp4 poster.png poster-square.png backup-cleaner-coverage.mp4; do cmp out-v3/$f ../videos/backup-cleaner-coverage/$f; done
```

In a dry run on a fresh clone on Oct 7, 2026: The silent loops, posters, and music version all rebuilt byte for byte.

## Rebuild checklist

| Item | Where it is |
|---|---|
| 1. Source files and art | [src/v3.html](../../src/v3.html). The painted background, screens, and text are all drawn in code in this one file, so there are no separate image files. Fonts are in [src/fonts/](../../src/fonts/), with download links in [src/README.md](../../src/README.md#fonts). |
| 2. Build scripts, tools, and versions | [src/render-v3.sh](../../src/render-v3.sh), [src/cap.js](../../src/cap.js), [src/make-music-version.sh](../../src/make-music-version.sh), [src/package.json](../../src/package.json), [src/package-lock.json](../../src/package-lock.json). Tool versions are in [src/README.md](../../src/README.md#tools-and-versions). |
| 3. Inputs: script and storyboard | [script.md](script.md). The sample data is written into [src/v3.html](../../src/v3.html). |
| 4. Step-by-step rebuild | "Rebuild from scratch" above, and [src/README.md](../../src/README.md#rebuild-from-scratch) |
| 5. Design rules | [docs/design-schema.md](../../docs/design-schema.md) and [docs/how-to-make-these-videos.md](../../docs/how-to-make-these-videos.md) |
| 6. Music credit and source | "Music credit" above. Source page: ["Rendezvous" by Shane Ivers](https://www.silvermansound.com/free-music/rendezvous). The audio file is not in this repo. |
| 7. Finished outputs | The two loops, two posters, and `backup-cleaner-coverage.mp4` in this folder |
| 8. Where it was shared | Below |

## Where it was shared

**Website.** The silent loops are on the My work page at https://airbnbai.rent/automate.html under the heading "Property managers: when a cleaner cancels, the next one gets asked." When checked on Oct 7, 2026, at about 8:36 PM PT, the loops on the page were byte for byte the same as the ones in this folder.

No social media posts found as of Oct 7, 2026.
