# Post-run analysis: Door codes for every guest, assigned and revoked automatically

Built on Oct 7, 2026. Rachael approved the video at about 4:27 PM PT and approved the door codes as rendered at about 4:32 PM PT that day. Times are Pacific Time.

## What was built

- A 10 second looping how-to video in two sizes, 1920x1080 and 1080x1080. Both are silent.
- A 20 second music version of the wide loop, for sharing.
- Two poster frames.
- The scene is one HTML file ([src/v6.html](../../src/v6.html)). It reuses the painted scene from the other videos and adds a painted front door with a smart lock keypad, a guest's phone, and a "Front door" card with a door codes table and an entry log. It has four numbered steps. All data on screen is sample data.

## About the door codes

The codes shown (4817, 2093, and 6352) are invented sample codes, and Rachael approved them as rendered on Oct 7, 2026. They are not codes for any real lock.

The video shows a setup that is meant to give each guest and contractor their own code, revoke it after checkout, and not reuse it. How well that holds up depends on the lock and the system behind it, which this video does not test.

## Render runs

| When (Oct 7, 2026, PT) | What | Result |
|---|---|---|
| Afternoon | Drafts and QC passes | Two layout fixes, listed below |
| About 4:08 PM | Final silent render | Both loops and both posters |
| About 4:10 PM | Music version | 20 s, "Parisian" |
| About 4:38 PM to 4:42 PM | Rebuild from the code in this repo, as a check | Both loops and both posters came out byte for byte the same. See "Source file" below. |

## Source file

After the final render, the working copy of the scene file was edited to use different sample codes. That edit is not in the published video. The copy in this repo puts back the codes that are in the video. The only differences between the two copies are seven code values: the code in the table (twice), the cleaner's code, the second guest's code, the code constant, the keypad key order, and the "REVOKED" message on the keypad.

A rebuild from the repo copy, with `src/render-v6.sh`, came out byte for byte the same as the published files for both loops and both posters. That suggests the repo copy matches the video, at least for these four files.

## QC checks and what they found

- **Frame review during the build.** Still frames from both loops at 0.2, 0.8, 1.5, 2.9, 3.9, 5.2, 6.0, 7.0, 7.9, 8.8, 9.4, and 9.95 seconds.
- **Frame check for the codes.** Frames were pulled from all three MP4 files at 1.7, 3.0, 5.6, 6.9, 7.9, and 9.3 seconds (and 10 seconds later in the music version), plus six evenly spaced frames from each file, and both posters were viewed. Findings:
  - The codes shown are 4817 (Dana K.), 2093 (Maria), and 6352 (Sam R.). No other settled code values were seen.
  - In the first second, the first code "rolls" through random digits before it lands on 4817. One of those passing values, 4185, can be seen in a single frame of the square loop at about 0.83 seconds. It is part of the animation, not a code.
  - The keypad lights 4, 8, 1, and 7, and later shows "4817 REVOKED".
- **Format check.** Both loops are H.264, `yuv420p`, 300 frames, 10.0 seconds. The music version is H.264 plus AAC stereo at 48 kHz, 600 frames, 20.0 seconds.
- **Music version matches the final loop.** The decoded video frames of both halves of the music version match the final wide loop frame for frame.
- **Posters match the loops.** Each poster matches frame 264 of its loop.
- **Loudness.** The music version measures about -16.4 LUFS integrated with a true peak of about -1.3 dBTP.
- **Privacy check before publishing.** Findings:
  - Person names: the sample guests "Dana K." and "Sam R." and the sample cleaner "Maria" (also "Dana's phone" and "WELCOME, DANA").
  - The welcome text comes from "La Maison" (avatar "LM"). Rachael decided on Oct 7, 2026 to keep "La Maison" on screen.
  - The keypad shows no lock brand.
  - No phone numbers, emails, street addresses, or Wi-Fi details were seen.
- **Metadata.** The MP4 files carry only standard encoder tags.

## Fixes made during the build

- The "Not reused" tag sat on top of the struck-through code. It moved inline, next to the status.
- The keypad "REVOKED" message ended too early to show on the poster. It now stays up until the loop fade, so the poster shows it.

## Output files

| File | Size | Details |
|---|---|---|
| `guest-door-codes.mp4` | 2.72 MB (2,716,973 bytes) | 1920x1080, 20 s, 30 fps, H.264 + AAC |
| `loop-1920x1080.mp4` | 1.11 MB (1,111,061 bytes) | 1920x1080, 10 s, 30 fps, H.264, no audio |
| `loop-1080x1080.mp4` | 723 KB (722,782 bytes) | 1080x1080, 10 s, 30 fps, H.264, no audio |
| `poster.png` | 1.80 MB (1,797,247 bytes) | Frame 264 (8.8 s) of the wide loop |
| `poster-square.png` | 844 KB (844,365 bytes) | Frame 264 (8.8 s) of the square loop |

## Still unverified

- The videos have not been checked on a range of real phones and browsers.
- The loop seam was checked on still frames, not by watching many loops in a row.
- The music version was made with the same steps as `src/make-music-version.sh`, but a rebuild of it from this repo has not been compared byte for byte.
- The video shows the idea of the setup. It does not show or test a real lock.

## What to improve next time

- Settle the sample codes before the final render, so the source and the video do not drift apart.
- Keep the source file read-only once a render is approved.
