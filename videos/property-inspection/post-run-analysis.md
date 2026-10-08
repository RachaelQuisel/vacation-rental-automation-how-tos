# Post-run analysis: When an inspection finds a problem, the right contractor is scheduled automatically

Built on Oct 7, 2026. The final render was made at about 8:35 PM PT, and Rachael approved adding the video to this repo at about 8:41 PM PT that day. Times are Pacific Time.

## What was built

- A 10 second looping how-to video in two sizes, 1920x1080 and 1080x1080. Both are silent.
- A 20 second music version of the wide loop, for sharing.
- Two poster frames.
- The scene is one HTML file ([src/v5.html](../../src/v5.html)). It reuses the painted scene, the four-step layout, and the motion of the other videos, and adds two phones (an inspector's checklist app and a contractor's text thread), a team chat window with a "# maintenance" channel, and text and email confirmation cards. All data on screen is sample data.

## How it differs from the other videos

- An earlier video in this slot was about back-office work. Rachael redefined it as a video just about property inspections, so this video replaced it. The earlier version is not in this repo.
- The cream panel is taller (top 170, bottom 912) to fit the long headline and steps.
- The headline is 54 px on three lines in wide and 44 px on two lines in square. The steps are placed 22 px under the measured bottom of the headline.
- The demo uses two phones side by side and a right-hand column for the chat window and cards. Exact positions are in the [design schema](../../docs/design-schema.md#layout-per-video) and the per-video notes in [How these videos are made](../../docs/how-to-make-these-videos.md).

## Render runs

| When (Oct 7, 2026, PT) | What | Result |
|---|---|---|
| Evening | Drafts and QC passes | Four fixes, listed below |
| About 8:35 PM | Final silent render and music version | Both loops, both posters, and the 20 s music version |
| About 8:50 PM to 9:00 PM | Rebuild from the code in this repo, as a check | Both loops, both posters, and the music version came out byte for byte the same |

## QC checks and what they found

- **Frame review.** Still frames from both loops at 0.2, 1.3, 2.0, 3.0, 3.4, 4.4, 5.4, 6.0, 7.3, 8.0, 8.8, 9.4, and 9.95 seconds.
- **Format check.** Both loops are H.264, 300 frames, 10.0 seconds. The music version is H.264 plus AAC stereo at 48 kHz, 600 video frames, 20.0 seconds.
- **Loudness.** The music version measures about -16.0 LUFS integrated with a true peak of about -1.3 dBTP.
- **Privacy check before publishing.** Findings:
  - Person names: only the invented names Nina L. (inspector), Marco R. (plumber), and Leo S. (spa tech). The scene file was also searched for the names of real people connected to the rental, and none were found.
  - The texts come from "La Maison" (avatar "LM"). Rachael decided on Oct 7, 2026 to keep "La Maison" on screen in these videos.
  - The chat window is styled like Slack but shows no logo and no handles.
  - No phone numbers, emails, street addresses, or door codes were seen in the posters or QC frames.
- **Metadata.** The MP4 files carry only standard encoder tags.

## Fixes made during the build

- The phones and the progress bar picked up styles from the layout they were copied from. Their class names were changed (`.phn`, `.pgb`, `.smp2`) so the styles no longer clash.
- The bottom sheet hid the flagged item in the final frame. It now slides away after sending, and the item shows "Plumber texted ✓".
- The paper note wrapped its ✓ to a second line. The note was widened.
- In square, the phones were enlarged from 0.78 to 0.9 scale, and the cards were stacked full width.

## Output files

| File | Size | Details |
|---|---|---|
| `property-inspection.mp4` | 2.89 MB (2,885,992 bytes) | 1920x1080, 20 s, 30 fps, H.264 + AAC |
| `loop-1920x1080.mp4` | 1.19 MB (1,189,533 bytes) | 1920x1080, 10 s, 30 fps, H.264, no audio |
| `loop-1080x1080.mp4` | 827 KB (827,336 bytes) | 1080x1080, 10 s, 30 fps, H.264, no audio |
| `poster.png` | 1.74 MB (1,737,962 bytes) | Frame 264 (8.8 s) of the wide loop |
| `poster-square.png` | 726 KB (726,178 bytes) | Frame 264 (8.8 s) of the square loop |

## Still unverified

- The videos have not been checked on a range of real phones and browsers.
- The loop seam was checked on still frames, not by watching many loops in a row.
- The video shows how the workflow is meant to work. It does not show or test a real checklist app, texting service, or chat app.

## What to improve next time

- Start a new scene file from shared styles, so copied class names can't clash.
