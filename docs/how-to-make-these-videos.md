# How these videos are made

This is a spec for making a short how-to video that matches the others in this repo. It is adapted from the build notes for the first video, made on Oct 7, 2026. It should be enough to make a close match, but expect to adjust layout numbers for your own steps.

Related docs:

- [Design schema](design-schema.md): palette, fonts, coordinates, filters, and timeline as tables.
- [Workflow diagrams](workflow.md): the production pipeline and the 10 second loop.
- [Build code](../src/): the scene file, frame capture, and render scripts for the cleaner video.

## Ground rules

- **Sample data only.** Every name, date, number, and link on screen is made up. No real guests, cleaners, phone numbers, emails, addresses, door codes, or tax IDs.
- **No caption line** under or inside the video. The headline and steps carry the message.
- **Hedged wording.** Avoid absolute claims such as "zero mistakes" or "never miss."
- **No AI video generators.** They tend to garble on-screen text. The scene is drawn in code instead, so every word stays sharp.
- **Original art.** The look is a soft, hand-painted style with warm afternoon light. No characters, scenes, or logos are copied from any film or brand.

## The recipe

### 1. Plan the content

- One headline. For example: "The smarter way to schedule your contractors."
- Three to five numbered steps that describe a real sequence. Use numbers only when the order matters.
- A demo surface that acts out each step, such as a phone, a laptop, or a tablet.
- Sample data that is internally consistent. For dates, pick a month where the weekdays line up. The cleaner video uses a June that starts on a Sunday and shows no year.

### 2. Design choices

- Ground the scene in the subject. The cleaner video shows a cottage on turnover day, a taped paper note, and handwriting, not a generic dashboard.
- Make the painted scene the one bold element. Keep the screens calm.
- Use two clearly different font families: Nunito for all interface and headline text, and Caveat for one handwritten note.
- Avoid common generated looks: no all-caps labels, no single highlighted word in the headline, no monospace data labels, and no grid of identical cards.
- Use motion only where something changes, such as a tap, a selection, or an event appearing.
- Keep button wording consistent. If the button says "Sign me up," the result should say "signed up."

### 3. Paint the scene in SVG

The background is drawn in code inside one HTML file. Three SVG filters give the painted look:

| Filter | Settings | Purpose |
|---|---|---|
| `wc` | fractalNoise, baseFrequency 0.012, 3 octaves, seed 4, displacement scale 22 | Wobbly watercolor edges on hills, cottage, flowers, grass, and the cream panel |
| `soft` | fractalNoise, baseFrequency 0.02, 2 octaves, seed 9, displacement scale 30, blur 2.2 | Billowy cloud edges |
| `grain` | fractalNoise, baseFrequency 0.9, 2 octaves, about 9% opacity | Faint paper texture over the whole frame |

Other scene parts:

- A sky gradient from `#9FCBE2` to `#D7E8E6` to `#F6E7C6`.
- A soft radial glow in `#FFE7B0` at the upper left for warm light.
- Three bougainvillea clusters of 70 small circles each, placed with a fixed number seed so they look the same on every frame.
- Four clouds that drift right and nine leaves and petals that drift across. Both wrap while off screen.

### 4. Palette

| Name | Hex |
|---|---|
| Ink navy | `#24344D` |
| Paper cream | `#FBF4E4` |
| Sand | `#F0E1C2` |
| Terracotta | `#C2643F` |
| Leaf green | `#5F8F55` |
| Deep green | `#2F5A44` |
| Clouds | `#FFF9EE` |
| Bougainvillea | `#C93F77`, `#E06A9A` |

The full list is in the [design schema](design-schema.md).

### 5. Text and timing

- Write all on-screen text as real HTML text, not as part of a picture.
- Write one function, `window.render(t)`, that sets every element to its exact state at time `t` in seconds. No timers and no CSS animations. This makes every frame repeatable.
- The loop is 10 seconds at 30 fps, so 300 frames.
- Sync the step highlight with the demo. When the demo moves to the next screen, the highlight moves to the next step.
- Use a smooth ease in-out curve for slides and a small overshoot curve for pop-ins.
- End the loop on a frame that matches frame 0. The cleaner video fades a blank copy of the first screen over everything from 9.0 to 9.6 seconds.

### 6. Wide and square layouts

- Wide is 1920x1080. Headline and steps sit on a cream panel on the left. The demo sits on the right.
- Square is 1080x1080 and comes from the same file. Adding `?sq` to the page address turns on a set of `body.sq` style rules. These shift the scene left, hide the cream panel, shrink the headline, and give every overlay its own position.
- Check that no text runs off the canvas and that no painted edge shows at the side.

### 7. Capture frames

Do not record the screen. Step through time instead:

1. Open the page in headless Chrome at the exact canvas size.
2. Wait for fonts to load.
3. For each frame `i`, call `render(i/30)` and save a PNG.

Use `--force-color-profile=srgb` so colors stay the same from run to run. Capture wide and square at the same time. Each capture took about 2 to 4 minutes on the build machine. See [src/cap.js](../src/cap.js).

### 8. Encode with ffmpeg

```bash
E="-c:v libx264 -pix_fmt yuv420p -preset slow -crf 22 -movflags +faststart -an"
ffmpeg -y -framerate 30 -i frames-wide/f%04d.png   $E loop-1920x1080.mp4
ffmpeg -y -framerate 30 -i frames-square/f%04d.png $E loop-1080x1080.mp4
```

- `libx264` with `yuv420p` plays in all common browsers.
- CRF 22 is the quality level. Lower numbers mean higher quality and bigger files.
- `+faststart` lets a web page start playing before the whole file downloads.
- `-an` leaves out audio, so the loops can autoplay muted.
- Aim to keep each loop under about 5 MB. The cleaner loops are about 1.06 MB (wide) and 705 KB (square).

### 9. Pick the poster frame

Use a frame where the story is complete. For the cleaner video that is frame 240 (8.0 seconds): the filled calendar, step 3, and the note are all on screen.

### 10. QC frame check

Pull still frames from each finished MP4 and look at every one. Check for clipped text, overlapping text, typos, readability, and anything that looks like real data.

```bash
for t in 0.2 1.8 3.5 4.8 6.3 8.0 9.4 9.95; do
  ffmpeg -y -ss $t -i loop-1920x1080.mp4 -frames:v 1 qc/wide-$t.png
  ffmpeg -y -ss $t -i loop-1080x1080.mp4 -frames:v 1 qc/square-$t.png
done
```

Pick times that cover every step and the loop reset. Give each round of QC frames new file names, so an image viewer does not show an old copy. Then confirm the format:

```bash
ffprobe -v error -show_entries stream=codec_name,pix_fmt,width,height -show_entries format=duration -of compact=p=0 loop-1920x1080.mp4
```

Expect `h264`, `yuv420p`, the right size, and 10.0 seconds. If anything is off, fix the HTML and repeat steps 7 to 10.

### 11. Music version

The shareable how-to is the wide loop played twice (20 seconds) with a music track. See [src/make-music-version.sh](../src/make-music-version.sh).

- Pick a track under a license that allows commercial and social use with credit, such as CC BY 4.0. Use a different track for each video.
- Pick a 20 second excerpt that starts on a bar downbeat. One way: find the loudest 20 second window, then snap the start to the nearest downbeat.
- Add a 0.3 second fade in and a 1.5 second fade out (18.5 to 20 seconds).
- Level it with two-pass ffmpeg `loudnorm` to about -16 LUFS, true peak -1.5 dB.
- Copy the video stream as is. Encode audio as AAC, 192 kbps, 48 kHz stereo, with `+faststart`.
- **CC BY requires credit.** Put the credit line next to the video everywhere it is published, such as the video's README or the post text. Do not commit the audio file itself. Link to its source page instead.

## Per-video notes

### Schedule your cleaners by text

Full detail is in [the script](../videos/schedule-cleaners-by-text/script.md) and [the post-run analysis](../videos/schedule-cleaners-by-text/post-run-analysis.md). In short:

- Headline: "The smarter way to schedule your contractors."
- Steps: 1. Your cleaner gets a text. 2. They pick the dates they want to clean. 3. They're signed up on your shared calendar.
- Demo surface: one phone with three screens (text thread, date picker, shared calendar) and a taped paper note.
- Sample data: one cleaner named Maria G. and four turnover dates in June.
- Music: "Le Croissant" by Shane Ivers, CC BY 4.0.

### Monthly TOT and TBID tax prep (coming soon)

Same recipe with five steps and a laptop as the demo surface. Sample payouts and charges go into a database, a script calculates the taxes, the numbers are mapped onto a sample tax form, and an audit step checks the totals.

### When your cleaner can't make it, the next one is asked automatically (coming soon)

Same recipe with four steps, a tablet calendar, and a phone. A sample cleaner declines a calendar invite, the next sample cleaner accepts, and the owner gets a text if a day still needs coverage.
