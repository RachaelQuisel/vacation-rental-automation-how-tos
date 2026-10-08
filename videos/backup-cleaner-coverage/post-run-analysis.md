# Post-run analysis: When your cleaner can't make it, the next one is asked automatically

Built on Oct 7, 2026, and marked final at about 4:13 PM PT that day. Times are Pacific Time.

## What was built

- A 10 second looping how-to video in two sizes, 1920x1080 and 1080x1080. Both are silent.
- A 20 second music version of the wide loop, for sharing.
- Two poster frames.
- The scene is one HTML file ([src/v3.html](../../src/v3.html)). It reuses the painted scene from the cleaner video and adds a painted guest room, a tablet with a cleaning calendar, and a phone. It has four numbered steps. All data on screen is sample data.

## Render runs

| When (Oct 7, 2026, PT) | What | Result |
|---|---|---|
| Afternoon | Earlier drafts: an email version with a "Fill this gap" button, then a text alert version | Replaced by an invite-and-reroute version that follows the real flow more closely |
| Afternoon | Messy room scene added at Rachael's request | Room grows, gets cleaned, and shrinks to an inset |
| About 3:59 PM to 4:04 PM | Final silent render | Both loops and both posters |
| About 4:04 PM | Music version | 20 s, "Rendezvous" |
| About 4:19 PM to 4:23 PM | Rebuild from the code in this repo, as a check | The wide loop and wide poster came out byte for byte the same. The square loop and square poster differ by tiny anti-aliasing changes on a few edges (largest pixel change 20 of 255). They look the same. |

## QC checks and what they found

- **Frame review during the build.** Still frames from both loops at 0.2, 0.8, 1.5, 2.3, 3.0, 4.0, 4.8, 5.6, 6.0, 6.5, 7.0, 7.6, 8.0, 8.8, 9.4, and 9.95 seconds. That covers every beat in both sizes. The messy room is clearest at 1.5 seconds.
- **Format check.** Both loops are H.264, `yuv420p`, 300 frames, 10.0 seconds. The music version is H.264 plus AAC stereo at 48 kHz, 20.0 seconds.
- **Music version matches the final loop.** The decoded video frames of both halves of the music version match the final wide loop frame for frame.
- **Loudness.** The music version measures about -16.1 LUFS integrated with a true peak of about -3.9 dBTP.
- **Privacy check before publishing.** Six evenly spaced frames were pulled from each of the three MP4 files, and both posters were viewed. Findings:
  - Person names: the sample cleaners "Maria G." and "Rosa P." (also "Maria", "Rosa", and the initials "MG" and "RP").
  - The calendar invite reads "Turnover at La Maison". Rachael decided on Oct 7, 2026 to keep "La Maison" on screen.
  - The text alert comes from "Alerts" and shows no phone number.
  - No phone numbers, emails, street addresses, door codes, or tax IDs were seen.
- **Real names check.** An early draft used a cleaner name that matched a real person. It was replaced with the sample name "Rosa P." everywhere in the source. A search of the source for the real team's first names found none.
- **Metadata.** The MP4 files carry only standard encoder tags.

## Fixes made during the build

- With the longer headline, the square paper note collided with it. The note moved under the tablet.
- In the room scene, the guests were made bigger, the dismay marks were moved so the door arch does not clip them, the sparkles were made bigger with more contrast, and a painting was added above the bed.
- A cleaner name that matched a real person was replaced with a sample name.

## Output files

| File | Size | Details |
|---|---|---|
| `backup-cleaner-coverage.mp4` | 3.58 MB (3,582,526 bytes) | 1920x1080, 20 s, 30 fps, H.264 + AAC |
| `loop-1920x1080.mp4` | 1.53 MB (1,529,894 bytes) | 1920x1080, 10 s, 30 fps, H.264, no audio |
| `loop-1080x1080.mp4` | 1.07 MB (1,065,286 bytes) | 1080x1080, 10 s, 30 fps, H.264, no audio |
| `poster.png` | 1.68 MB (1,677,406 bytes) | Frame 264 (8.8 s) of the wide loop |
| `poster-square.png` | 685 KB (684,664 bytes) | Frame 264 (8.8 s) of the square loop |

## Still unverified

- The videos have not been checked on a range of real phones and browsers.
- The loop seam was checked on still frames, not by watching many loops in a row.
- The square version does not rebuild byte for byte. The difference looks like small font or edge rendering changes between runs, but the exact cause has not been confirmed.
- The music version was made with the same steps as `src/make-music-version.sh`, but a rebuild of it from this repo has not been compared byte for byte.

## What to improve next time

- Check every sample name against the real team list before the first render, not after.
- Look into why the square render can vary slightly between runs, for example by fixing transforms to whole pixels.
- This is the largest of the three videos. A slightly higher CRF for the square loop could bring it closer to the others.
