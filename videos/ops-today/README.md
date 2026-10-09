# A morning briefing in Slack so your whole team starts the day on the same page

Every morning, a briefing is built automatically and posted to your team's Slack channel before the workday starts: alerts, bookings, reviews, money, guest messages, and cleaning coverage in one post, so everyone sees the same plan.

Uses sample data. The names, dates, amounts, and events in the video are made up.

## Files

| File | What it is |
|---|---|
| [ops-today.mp4](ops-today.mp4) | The main how-to video. 1920x1080, 20 seconds, with music. |
| [loop-1920x1080.mp4](loop-1920x1080.mp4) | Silent 10 second loop, wide. Made for a website. |
| [loop-1080x1080.mp4](loop-1080x1080.mp4) | Silent 10 second loop, square. Made for phones and social posts. |
| [poster.png](poster.png) | Still frame for the wide video (8.8 seconds in). |
| [poster-square.png](poster-square.png) | Still frame for the square video (8.8 seconds in). |
| [script.md](script.md) | On-screen script and storyboard, beat by beat. |
| [post-run-analysis.md](post-run-analysis.md) | How this video was built, checked, and fixed, plus open items. |
| [field-guide.md](field-guide.md) | Every label on screen, what each teammate sees, and a short FAQ. |

## Music credit

The music is in `ops-today.mp4` only. The two loops are silent.

```
"Suave Standpipe" Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 4.0
http://creativecommons.org/licenses/by/4.0/
```

Links: [incompetech.com](https://incompetech.com), [track page](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1500078), [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/)

The track was cut to a 20 second excerpt, faded in and out, and leveled for loudness. If you share this video, please keep this credit with it.

## How it was made

See [How these videos are made](../../docs/how-to-make-these-videos.md) and the build code in [src/](../../src/).

## Rebuild from scratch

Full prerequisites, tool versions, and font setup are in [src/README.md](../../src/README.md#rebuild-from-scratch). For this video only:

```bash
git clone https://github.com/RachaelQuisel/vacation-rental-automation-how-tos.git
cd vacation-rental-automation-how-tos/src
npm ci
mkdir -p ~/.local/share/fonts && cp fonts/*.ttf ~/.local/share/fonts/ && fc-cache -f   # Linux: install the fonts (macOS: see src/README.md)

# Silent loops, posters (frame 264, 8.8 seconds), and QC frames, in src/out-v7/
./render-v7.sh

# Music version. The audio file is not in this repo, so download it first.
mkdir -p music
curl -L -o music/suave-standpipe.mp3 "https://incompetech.com/music/royalty-free/mp3-royaltyfree/Suave%20Standpipe.mp3"
./make-music-version.sh out-v7/loop-1920x1080.mp4 music/suave-standpipe.mp3 86.39 out-v7/ops-today.mp4

# Compare with the committed files. cmp prints nothing when they match.
for f in loop-1920x1080.mp4 loop-1080x1080.mp4 poster.png poster-square.png ops-today.mp4; do cmp out-v7/$f ../videos/ops-today/$f; done
```

In a dry run on Oct 7, 2026: the silent loops, posters, and music version all rebuilt byte for byte.

## Rebuild checklist

| Item | Where it is |
|---|---|
| 1. Source files and art | [src/v7.html](../../src/v7.html). The painted background, screens, and text are all drawn in code in this one file, so there are no separate image files. Fonts are in [src/fonts/](../../src/fonts/), with download links in [src/README.md](../../src/README.md#fonts). |
| 2. Build scripts, tools, and versions | [src/render-v7.sh](../../src/render-v7.sh), [src/cap.js](../../src/cap.js), [src/make-music-version.sh](../../src/make-music-version.sh), [src/package.json](../../src/package.json), [src/package-lock.json](../../src/package-lock.json). Tool versions are in [src/README.md](../../src/README.md#tools-and-versions). |
| 3. Inputs: script and storyboard | [script.md](script.md). The sample data is written into [src/v7.html](../../src/v7.html). |
| 4. Step-by-step rebuild | "Rebuild from scratch" above, and [src/README.md](../../src/README.md#rebuild-from-scratch) |
| 5. Design rules | [docs/design-schema.md](../../docs/design-schema.md) and [docs/how-to-make-these-videos.md](../../docs/how-to-make-these-videos.md) |
| 6. Music credit and source | "Music credit" above. Source page: ["Suave Standpipe" by Kevin MacLeod](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1500078). The audio file is not in this repo. |
| 7. Finished outputs | The two loops, two posters, and `ops-today.mp4` in this folder |
| 8. Where it was shared | Below |

## Where it was shared

It went live on the My work page at https://airbnbai.rent/automate.html on Oct 7, 2026. The change was merged at 10:58 PM PT. When checked at about 11:04 PM PT, the loops on the page were byte for byte the same as the ones in this folder.
