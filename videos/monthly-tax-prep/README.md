# Monthly TOT and TBID tax prep

Payouts and charges from your booking platforms land in a database, a script calculates TOT and TBID, maps the numbers onto the city tax form, and an audit script checks the totals add up.

Uses sample data. The bookings, amounts, and account number in the video are made up. TOT is the transient occupancy tax, and TBID is the tourism business improvement district assessment.

## Files

| File | What it is |
|---|---|
| [monthly-tax-prep.mp4](monthly-tax-prep.mp4) | The main how-to video. 1920x1080, 20 seconds, with music. |
| [loop-1920x1080.mp4](loop-1920x1080.mp4) | Silent 10 second loop, wide. Made for a website. |
| [loop-1080x1080.mp4](loop-1080x1080.mp4) | Silent 10 second loop, square. Made for phones and social posts. |
| [poster.png](poster.png) | Still frame for the wide video (8.8 seconds in). |
| [poster-square.png](poster-square.png) | Still frame for the square video (8.8 seconds in). |
| [script.md](script.md) | On-screen script and storyboard, beat by beat. |
| [post-run-analysis.md](post-run-analysis.md) | How this video was built, checked, and fixed, plus open items. |
| [field-guide.md](field-guide.md) | Every label on screen, how each person sees the system, and a short FAQ. |

## Music credit

The music is in `monthly-tax-prep.mp4` only. The two loops are silent.

Music: "La Pompe Du Trompe" by Shane Ivers ([silvermansound.com](https://www.silvermansound.com)), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

The track was cut to a 20 second excerpt, faded in and out, and leveled for loudness. If you share this video, please keep this credit line with it.

## How it was made

See [How these videos are made](../../docs/how-to-make-these-videos.md) and the build code in [src/](../../src/) (`v2.html` and `render-v2.sh`).

## Rebuild from scratch

Full prerequisites, tool versions, and font setup are in [src/README.md](../../src/README.md#rebuild-from-scratch). For this video only:

```bash
git clone https://github.com/RachaelQuisel/vacation-rental-automation-how-tos.git
cd vacation-rental-automation-how-tos/src
npm ci
mkdir -p ~/.local/share/fonts && cp fonts/*.ttf ~/.local/share/fonts/ && fc-cache -f   # Linux: install the fonts (macOS: see src/README.md)

# Silent loops, posters (frame 264, 8.8 seconds), and QC frames, in src/out-v2/
./render-v2.sh

# Music version. The audio file is not in this repo, so download it first.
mkdir -p music
curl -L -o music/la-pompe-du-trompe.mp3 https://www.silvermansound.com/wp-content/uploads/la-pompe-du-trompe.mp3
./make-music-version.sh out-v2/loop-1920x1080.mp4 music/la-pompe-du-trompe.mp3 87.42 out-v2/monthly-tax-prep.mp4

# Compare with the committed files. cmp prints nothing when they match.
for f in loop-1920x1080.mp4 loop-1080x1080.mp4 poster.png poster-square.png monthly-tax-prep.mp4; do cmp out-v2/$f ../videos/monthly-tax-prep/$f; done
```

In a dry run on a fresh clone on Oct 7, 2026: The silent loops, posters, and music version all rebuilt byte for byte.

## Rebuild checklist

| Item | Where it is |
|---|---|
| 1. Source files and art | [src/v2.html](../../src/v2.html). The painted background, screens, and text are all drawn in code in this one file, so there are no separate image files. Fonts are in [src/fonts/](../../src/fonts/), with download links in [src/README.md](../../src/README.md#fonts). |
| 2. Build scripts, tools, and versions | [src/render-v2.sh](../../src/render-v2.sh), [src/cap.js](../../src/cap.js), [src/make-music-version.sh](../../src/make-music-version.sh), [src/package.json](../../src/package.json), [src/package-lock.json](../../src/package-lock.json). Tool versions are in [src/README.md](../../src/README.md#tools-and-versions). |
| 3. Inputs: script and storyboard | [script.md](script.md). The sample data is written into [src/v2.html](../../src/v2.html). |
| 4. Step-by-step rebuild | "Rebuild from scratch" above, and [src/README.md](../../src/README.md#rebuild-from-scratch) |
| 5. Design rules | [docs/design-schema.md](../../docs/design-schema.md) and [docs/how-to-make-these-videos.md](../../docs/how-to-make-these-videos.md) |
| 6. Music credit and source | "Music credit" above. Source page: ["La Pompe Du Trompe" by Shane Ivers](https://www.silvermansound.com/free-music/la-pompe-du-trompe). The audio file is not in this repo. |
| 7. Finished outputs | The two loops, two posters, and `monthly-tax-prep.mp4` in this folder |
| 8. Where it was shared | Below |

## Where it was shared

**Website.** The silent loops are on the My work page at https://airbnbai.rent/automate.html. When checked on Oct 7, 2026, at about 8:36 PM PT, the loops on the page were byte for byte the same as the ones in this folder.

No social media posts found as of Oct 7, 2026.
