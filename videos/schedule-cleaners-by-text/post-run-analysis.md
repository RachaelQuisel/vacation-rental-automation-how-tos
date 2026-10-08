# Post-run analysis: Schedule your cleaners by text

Built and approved on Oct 7, 2026. Times are Pacific Time.

## What was built

- A 10 second looping how-to video in two sizes, 1920x1080 and 1080x1080. Both are silent.
- A 20 second music version of the wide loop, for sharing.
- Two poster frames.
- The scene is one HTML file ([src/v1.html](../../src/v1.html)) with a painted SVG background, a phone with three screens, a headline, three numbered steps, and a taped paper note. All data on screen is sample data.

## Render runs

| When (Oct 7, 2026, PT) | What | Result |
|---|---|---|
| About 10:00 AM to 12:00 PM | Early drafts and test stills | Several layout problems found (see fixes below) |
| About 12:14 PM to 12:18 PM | Final silent render after the caption was removed | `loop-1920x1080.mp4` and `loop-1080x1080.mp4`, posters, QC frames |
| About 2:57 PM | Music version | `schedule-cleaners-by-text.mp4`, 20 s |
| About 3:55 PM to 3:59 PM | Rebuild from the code in this repo, as a check | Both loops and both posters came out byte for byte the same as the published files |

## QC checks and what they found

- **Frame review during the build.** Still frames were pulled from both loops at 0.2, 1.8, 3.5, 4.8, 6.3, 8.0, 9.4, and 9.95 seconds. These cover every step and the loop reset. After the caption was removed, a shorter check at 0.2, 1.8, 4.8, and 8.0 seconds was run on the final render.
- **Format check.** ffprobe shows H.264, `yuv420p`, the right size, and 10.0 seconds for both loops. The music version is H.264 plus AAC stereo at 48 kHz, 20.0 seconds.
- **Loudness.** The music version measures about -16.5 LUFS integrated with a true peak of about -6.7 dBTP. The target was -16 LUFS, so this looks close enough.
- **Privacy check before publishing.** Six evenly spaced frames were pulled from each of the three MP4 files, and both posters were viewed. No phone numbers, emails, street addresses, door codes, tax IDs, or repo names were seen. The only person name is the sample cleaner "Maria" / "Maria G." The sender name on the text thread is "La Maison Turnovers," and the sample link is `lmsb.co/pick`.
- **Metadata.** The MP4 files carry only standard encoder tags. No titles, paths, or other text were found in them.

## Fixes made during the build

- An earlier caption line under the scene was removed on Oct 7, 2026, at the owner's request. The video now has no caption.
- Old flow labels overlapped the paragraph text. The paragraph and labels were later replaced by the three numbered steps.
- Tap ripples landed in the wrong place. The fix measures each tapped element on screen and places the ripple at its center.
- Clouds visibly popped back in when they wrapped. The wrap distance was widened to 2800 px with a 450 px offset, so clouds wrap off screen.
- The first square layout left the phone off the canvas. The square version now has its own position for every overlay.
- A thin unpainted strip showed at the right edge of the square version. The scene shift was changed from 840 to 790 px.
- The loop reset showed three screens blended together. One blank thread screen now fades in over everything.
- The longer headline crowded the steps. The headline was reduced to 72 px and its column widened to 680 px.
- Step 3 wrapped to two lines in the wide version. Steps were set to 29 px on one line in a 736 px column, and the cream panel was widened.
- The cream panel edge showed behind the phone in the square version. The panel is now hidden in the square version.
- A job tag covered the cottage in the wide version. It was replaced by the paper note, which sits in the sky in wide and on the grass in square.
- An image viewer once showed an older copy of a reused QC file name. Each round of QC frames now gets new file names.

## Output files

| File | Size | Details |
|---|---|---|
| `schedule-cleaners-by-text.mp4` | 2.61 MB (2,610,578 bytes) | 1920x1080, 20 s, 30 fps, H.264 + AAC 192 kbps |
| `loop-1920x1080.mp4` | 1.06 MB (1,057,827 bytes) | 1920x1080, 10 s, 30 fps, H.264, no audio |
| `loop-1080x1080.mp4` | 705 KB (704,572 bytes) | 1080x1080, 10 s, 30 fps, H.264, no audio |
| `poster.png` | 1.79 MB (1,792,704 bytes) | Frame 240 of the wide loop |
| `poster-square.png` | 869 KB (869,456 bytes) | Frame 240 of the square loop |

## Still unverified

- The videos have not been checked on a range of real phones and browsers. Autoplay, looping, and color may vary.
- The loop seam was checked on still frames, not by watching many loops in a row.
- `make-music-version.sh` makes a close match to the published music version, but not a byte-for-byte copy. The published file was made with an earlier form of the same steps. In a test on Oct 7, 2026, the script's output measured about -16.1 LUFS, and its video stream did not match byte for byte.
- It has not been checked whether `lmsb.co` is a registered domain. It is meant only as a sample link.
- The posters are PNG files of about 0.9 to 1.8 MB. A website would likely want smaller WebP or JPEG copies.

## What to improve next time

- Use a reserved sample domain such as `example.com` for on-screen links, so the link cannot point to a real site.
- Keep the music step as a script from the start, so the published music version can be rebuilt exactly.
- Make a contact sheet of QC frames automatically, so one image covers the whole loop.
- Add an automated text scan of the HTML for anything that looks like a phone number, email, or address before rendering.
- Pin the Chrome version along with `playwright-core`, since font rendering can change between versions.
