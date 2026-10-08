# Schedule your cleaners by text

Your cleaner gets a text, picks the dates they want to clean, and is signed up on your shared calendar.

Uses sample data. The names, dates, and link in the video are made up.

## Files

| File | What it is |
|---|---|
| [schedule-cleaners-by-text.mp4](schedule-cleaners-by-text.mp4) | The main how-to video. 1920x1080, 20 seconds, with music. |
| [loop-1920x1080.mp4](loop-1920x1080.mp4) | Silent 10 second loop, wide. Made for a website. |
| [loop-1080x1080.mp4](loop-1080x1080.mp4) | Silent 10 second loop, square. Made for phones and social posts. |
| [poster.png](poster.png) | Still frame for the wide video (8.0 seconds in). |
| [poster-square.png](poster-square.png) | Still frame for the square video (8.0 seconds in). |
| [script.md](script.md) | On-screen script and storyboard, beat by beat. |
| [post-run-analysis.md](post-run-analysis.md) | How this video was built, checked, and fixed, plus open items. |
| [field-guide.md](field-guide.md) | Every label on screen, how each person sees the system, and a short FAQ. |

## Music credit

The music is in `schedule-cleaners-by-text.mp4` only. The two loops are silent.

Music: "Le Croissant" by Shane Ivers ([silvermansound.com](https://www.silvermansound.com)), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

The track was cut to a 20 second excerpt, faded in and out, and leveled for loudness. If you share this video, please keep this credit line with it.

## How it was made

See [How these videos are made](../../docs/how-to-make-these-videos.md) and the build code in [src/](../../src/).

## Rebuild from scratch

Full prerequisites, tool versions, and font setup are in [src/README.md](../../src/README.md#rebuild-from-scratch). For this video only:

```bash
git clone https://github.com/RachaelQuisel/vacation-rental-automation-how-tos.git
cd vacation-rental-automation-how-tos/src
npm ci
export FONTCONFIG_FILE="$PWD/fonts/fonts.conf"   # optional, Linux: use only the bundled fonts

# Silent loops, posters (frame 240 (8.0 seconds)), and QC frames, in src/out/
./render-v1.sh

# Music version. The audio file is not in this repo, so download it first.
mkdir -p music
curl -L -o music/le-croissant.mp3 https://www.silvermansound.com/wp-content/uploads/le-croissant.mp3
./make-music-version.sh out/loop-1920x1080.mp4 music/le-croissant.mp3 76.95 out/schedule-cleaners-by-text.mp4

# Compare with the committed files. cmp prints nothing when they match.
for f in loop-1920x1080.mp4 loop-1080x1080.mp4 poster.png poster-square.png schedule-cleaners-by-text.mp4; do cmp out/$f ../videos/schedule-cleaners-by-text/$f; done
```

In a dry run on a fresh clone on Oct 7, 2026: The silent loops and posters rebuilt byte for byte. The music version is a close match, not byte for byte (see [post-run-analysis.md](post-run-analysis.md)).

## Rebuild checklist

| Item | Where it is |
|---|---|
| 1. Source files and art | [src/v1.html](../../src/v1.html). The painted background, screens, and text are all drawn in code in this one file, so there are no separate image files. Fonts are in [src/fonts/](../../src/fonts/), with download links in [src/README.md](../../src/README.md#fonts). |
| 2. Build scripts, tools, and versions | [src/render-v1.sh](../../src/render-v1.sh), [src/cap.js](../../src/cap.js), [src/make-music-version.sh](../../src/make-music-version.sh), [src/package.json](../../src/package.json), [src/package-lock.json](../../src/package-lock.json). Tool versions are in [src/README.md](../../src/README.md#tools-and-versions). |
| 3. Inputs: script and storyboard | [script.md](script.md). The sample data is written into [src/v1.html](../../src/v1.html). |
| 4. Step-by-step rebuild | "Rebuild from scratch" above, and [src/README.md](../../src/README.md#rebuild-from-scratch) |
| 5. Design rules | [docs/design-schema.md](../../docs/design-schema.md) and [docs/how-to-make-these-videos.md](../../docs/how-to-make-these-videos.md) |
| 6. Music credit and source | "Music credit" above. Source page: ["Le Croissant" by Shane Ivers](https://www.silvermansound.com/free-music/le-croissant). The audio file is not in this repo. |
| 7. Finished outputs | The two loops, two posters, and `schedule-cleaners-by-text.mp4` in this folder |
| 8. Where it was shared | Below |

## Where it was shared

**LinkedIn.** Posted on Rachael's personal profile on Oct 7, 2026, at about 3:11 PM PT (the time is decoded from the post's activity ID). The post is about her cleaner scheduling app.

Link: https://www.linkedin.com/feed/update/urn:li:activity:7513722773966614528/

Post text, as published:

> The most important thing to do to ensure you have a multi-million dollar earning rental property is simple to understand but hard to do: fast, reliable communication. I built this app because it's faster and more reliable than I am, and it's why our guests always show up to a professionally cleaned house. Eleven years since founding La Maison, and I've built a lot of tools like this. I'm officially sharing out my expertise now at https://airbnbai.rent/ How do other Airbnb and Vrbo hosts manage the chaos of cleaner scheduling?

Tone notes:

- First person and confident, and it opens with a bold claim.
- One concrete benefit: guests always arrive to a professionally cleaned house.
- Credibility from 11 years since founding La Maison.
- One link, to airbnbai.rent.
- It closes with a question that invites comments from other Airbnb and Vrbo hosts.
- About 75 words in a single paragraph, with no hashtags or emoji. Rachael says LinkedIn doesn't use hashtags anymore.

An earlier draft was about 120 words, with a numbered three-step list. Rachael chose to post the shorter single-paragraph version.

If the music version is shared with the post, keep the credit line with it: Music: "Le Croissant" by Shane Ivers (silvermansound.com), CC BY 4.0.

**Website.** The silent loops are on the My work page at https://airbnbai.rent/automate.html under the heading "Property managers, tired of chasing cleaners and calendars?" When checked on Oct 7, 2026, at about 8:36 PM PT, the loops on the page were byte for byte the same as the ones in this folder.
