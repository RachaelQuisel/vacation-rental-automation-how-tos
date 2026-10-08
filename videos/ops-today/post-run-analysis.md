# Post-run analysis: A morning briefing in Slack so your whole team starts the day on the same page

Built on Oct 7, 2026. The final silent render was made at about 8:53 PM PT and the music version at about 8:55 PM PT. Rachael approved adding the video to this repo at about 10:42 PM PT that day. Times are Pacific Time.

## What was built

- A 10 second looping how-to video in two sizes, 1920x1080 and 1080x1080. Both are silent.
- A 20 second music version of the wide loop, for sharing.
- Two poster frames.
- The scene is one HTML file ([src/v7.html](../../src/v7.html)). It reuses the painted scene, the four-step layout, and the motion of the other videos, and adds a large team chat window with an "# ops-today" channel and a column of three teammate cards. All data on screen is sample data.

## How it differs from the other videos

- The cream panel is taller (top 170, bottom 912) to fit the long headline and steps.
- The headline is 56 px on three lines in wide and 42 px on two lines in square. The steps are placed 24 px under the measured bottom of the headline.
- New class names (prefixed `o` and `tm`) avoid clashes with styles the layout was copied from.
- Exact positions are in the [design schema](../../docs/design-schema.md#layout-per-video) and the per-video notes in [How these videos are made](../../docs/how-to-make-these-videos.md).

## Render runs

| When (Oct 7, 2026, PT) | What | Result |
|---|---|---|
| Evening | Drafts and QC passes | Four fixes, listed below |
| About 8:53 PM | Final silent render | Both loops and both posters |
| About 8:55 PM | Music version | 20 s, "Suave Standpipe" |
| About 10:44 PM to 10:46 PM | Rebuild from the code in this repo, as a check | Both loops, both posters, and the music version came out byte for byte the same |

## QC checks and what they found

- **Frame review.** Still frames from both loops at 0.2, 1.0, 2.0, 2.6, 3.1, 3.6, 4.95, 5.95, 6.2, 7.4, 8.1, 8.8, 9.4, and 9.95 seconds.
- **Format check.** Both loops are H.264, 300 frames, 10.0 seconds. The music version is H.264 plus AAC stereo at 48 kHz, 600 video frames, 20.0 seconds.
- **Loudness.** The music version measures about -16.0 LUFS integrated with a true peak of about -7.0 dBTP.
- **Wording.** The steps were checked for absolute claims, and two were softened (see [script.md](script.md)).
- **Metadata.** The MP4 files carry only standard encoder tags.

## Fixes made during the build

- The "Posted" toast first sat in the channel header on top of the "Sample data" tag. It moved down to the faded "yesterday" row.
- The empty "Seen by" row showed while the post was still being built. It now appears when the post goes out.
- In square, the "Seen ✓" chips overlapped the for-you line on the shorter cards. They moved to the top right of each card.
- The chat window was shortened from 800 to 720 px to remove empty space under the post.

## Output files

| File | Size | Details |
|---|---|---|
| `ops-today.mp4` | 3.05 MB (3,045,186 bytes) | 1920x1080, 20 s, 30 fps, H.264 + AAC |
| `loop-1920x1080.mp4` | 1.27 MB (1,271,023 bytes) | 1920x1080, 10 s, 30 fps, H.264, no audio |
| `loop-1080x1080.mp4` | 889 KB (889,456 bytes) | 1080x1080, 10 s, 30 fps, H.264, no audio |
| `poster.png` | 1.61 MB (1,613,734 bytes) | Frame 264 (8.8 s) of the wide loop |
| `poster-square.png` | 685 KB (685,188 bytes) | Frame 264 (8.8 s) of the square loop |

## Still unverified

- The videos have not been checked on a range of real phones and browsers.
- The loop seam was checked on still frames, not by watching many loops in a row.
- The video shows how the briefing is meant to work. It does not show or test a real chat app or the system that builds the briefing.

## What to improve next time

- Start a new scene file from shared styles, so copied class names can't clash.
