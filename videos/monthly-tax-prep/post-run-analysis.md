# Post-run analysis: Monthly TOT and TBID tax prep

Built on Oct 7, 2026, and marked final at about 4:13 PM PT that day. Times are Pacific Time.

## What was built

- A 10 second looping how-to video in two sizes, 1920x1080 and 1080x1080. Both are silent.
- A 20 second music version of the wide loop, for sharing.
- Two poster frames.
- The scene is one HTML file ([src/v2.html](../../src/v2.html)). It reuses the painted scene from the cleaner video and adds a laptop with three screens: a tax prep database, a calculation script, and a sample city tax form. It has five numbered steps. All data on screen is sample data.

## Render runs

| When (Oct 7, 2026, PT) | What | Result |
|---|---|---|
| Afternoon | First draft with three steps (report cards, total tiles, form) | Replaced by a five-step version that follows the real flow more closely |
| Afternoon | Five-step drafts | Layout fixes (see below) |
| About 4:00 PM to 4:03 PM | Final silent render | Both loops and both posters |
| About 4:04 PM | Music version | 20 s, "La Pompe Du Trompe" |
| About 4:15 PM to 4:19 PM | Rebuild from the code in this repo, as a check | Both loops and both posters came out byte for byte the same as the published files |

## QC checks and what they found

- **Frame review during the build.** Still frames from both loops at 0.2, 1.3, 2.8, 4.6, 6.4, 8.0, 8.8, 9.4, and 9.95 seconds.
- **Format check.** Both loops are H.264, `yuv420p`, 300 frames, 10.0 seconds. The music version is H.264 plus AAC stereo at 48 kHz, 20.0 seconds.
- **Music version matches the final loop.** The decoded video frames of both halves of the music version match the final wide loop frame for frame.
- **Loudness.** The music version measures about -16.0 LUFS integrated with a true peak of about -3.2 dBTP.
- **Privacy check before publishing.** Six evenly spaced frames were pulled from each of the three MP4 files, and both posters were viewed at full size. Findings:
  - The form header reads "City of Santa Barbara, TOT & TBID Monthly Return", with a "Sample, invented numbers" tag.
  - The business name field shows "La Maison". Rachael decided on Oct 7, 2026 to keep "La Maison" on screen. An earlier render briefly used a made-up name instead.
  - The TOT account field shows "SAMPLE-0001".
  - The dollar amounts are invented and add up (income $10,240.00, TOT $1,228.80, TBID $204.80, total $1,433.60).
  - No person names, phone numbers, emails, street addresses, real account or permit numbers, or tax IDs were seen.
- **Metadata.** The MP4 files carry only standard encoder tags.

## Fixes made during the build

- The fourth script line was pushed off screen because a class name clashed with older CSS. The class was renamed.
- Tick marks on the left column of the form crowded the right column. The ticks moved inside each row, and the form text was set to 15 px.
- In the square version, the paper note covered the "Totals match" badge. The note moved to the top right, next to the headline.
- The script lines were sped up, so the total stays on screen for a moment before the form slides up.
- The cream panel was made taller to fit five steps.

## Output files

| File | Size | Details |
|---|---|---|
| `monthly-tax-prep.mp4` | 2.90 MB (2,904,671 bytes) | 1920x1080, 20 s, 30 fps, H.264 + AAC |
| `loop-1920x1080.mp4` | 1.19 MB (1,188,698 bytes) | 1920x1080, 10 s, 30 fps, H.264, no audio |
| `loop-1080x1080.mp4` | 757 KB (756,550 bytes) | 1080x1080, 10 s, 30 fps, H.264, no audio |
| `poster.png` | 1.61 MB (1,612,117 bytes) | Frame 264 (8.8 s) of the wide loop |
| `poster-square.png` | 690 KB (690,456 bytes) | Frame 264 (8.8 s) of the square loop |

## Still unverified

- The tax rates (12% TOT and 2% TBID) were taken from the city's website during the build. They have not been rechecked since.
- The sample form is a simplified version of a city form. It is not the official form and should not be used for filing.
- The videos have not been checked on a range of real phones and browsers.
- The loop seam was checked on still frames, not by watching many loops in a row.
- The music version was made with the same steps as `src/make-music-version.sh`, but a rebuild of it from this repo has not been compared byte for byte.

## What to improve next time

- Keep the sample business and account fields obviously fake from the first draft.
- Keep a short note in the video folder with the source of each tax rate and the date it was checked.
- Check that new class names do not clash with shared CSS before rendering.
