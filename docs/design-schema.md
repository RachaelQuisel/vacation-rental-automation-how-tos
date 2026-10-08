# Design schema

This is the design system behind the how-to videos, written as tables. Most values come from the cleaner scheduling video ([src/v1.html](../src/v1.html)). The tax prep ([src/v2.html](../src/v2.html)) backup cleaner ([src/v3.html](../src/v3.html)), and door codes ([src/v6.html](../src/v6.html)) videos reuse the palette, fonts, filters, and motion, and change the layout to fit their steps. See [Layout per video](#layout-per-video).

## Canvas

| Version | Size (px) | Length | Frame rate | Audio | Use |
|---|---|---|---|---|---|
| Wide loop | 1920x1080 | 10 s | 30 fps (300 frames) | None | Website hero or section |
| Square loop | 1080x1080 | 10 s | 30 fps (300 frames) | None | Phones and social posts |
| Music version | 1920x1080 | 20 s (loop plays twice) | 30 fps | AAC stereo, 48 kHz, 192 kbps | Shareable how-to |

The square version is the same HTML file with `?sq` added to the address. That turns on the `body.sq` style rules.

## Palette

| Name | Hex | Used for |
|---|---|---|
| Ink navy | `#24344D` | Headline and active text |
| Paper cream | `#FBF4E4` | Cream panel, paper note, step number fill |
| Sand | `#F0E1C2` | Step highlight bar |
| Terracotta | `#C2643F` | Roof, active step number, avatar, tap ripple |
| Leaf green | `#5F8F55` | Front meadow, selected rows, calendar events |
| Deep green | `#2F5A44` | Button, handwritten note text |
| Sky top / middle / bottom | `#9FCBE2` / `#D7E8E6` / `#F6E7C6` | Sky gradient (stops at 0, 0.6, 1) |
| Sun glow | `#FFE7B0` | Radial glow, upper left, 75% opacity fading to 0 |
| Cloud | `#FFF9EE` | Cloud fill (shadow `#C9D6E0` at 55%) |
| Bougainvillea | `#C93F77`, `#E06A9A` | Flower clusters (leaves `#4E7F4A`) |
| Far hills | `#9DB89A`, `#7FA36F` | Back hills |
| Near meadow | `#5F8F55`, `#46754A` | Front grass bands |
| Cottage | wall `#F7EBD3`, roof edge `#9B4A2C`, windows `#5C7F92`, door `#3F6B57` | Cottage shapes |
| Phone frame | `#2B3A52` (inner line `#43557A`) | Phone body |
| Phone screen | `#FDF8EE` | Screen background |
| Text bubble | `#EDE4D1` | Incoming text message |
| Link | `#1F5E8C` | Link in the text message |
| Muted text | `#7D879A`, `#7A8597`, `#8A93A3` | Inactive steps, sub labels, day names |
| Selected row | border `#5F8F55`, fill `#EEF4E7` | Picked dates |
| Calendar cell | `#F4ECDC` | Empty day |
| Open slot | `#D9C9A8` on text `#6B5B3F` | "Open" chips |
| Tape | `rgba(214,196,160,.75)` | Tape on the paper note |

## Fonts

| Font | Weight | Size wide / square | Used for |
|---|---|---|---|
| Nunito | 800 | 72 px / 56 px, line height 1.02, letter spacing -1.5 px | Headline |
| Nunito | 700 | 29 px / 25 px | Step text |
| Nunito | 800 | 25 px / 21 px | Step numbers |
| Nunito | 600 to 800 | 13 px to 29 px | Phone screen text |
| Caveat | Regular | 44 px / 40 px | Handwritten paper note |

Both fonts are free Google Fonts. They are installed as system fonts, and the page names them without downloading them.

## Layout coordinates

All values are CSS pixels inside the canvas.

| Element | Wide (1920x1080) | Square (1080x1080) |
|---|---|---|
| Painted scene | Full canvas | Shifted 790 px left |
| Cream panel | Wobbly shape from about x 90 to 890, y 206 to 866 | Hidden |
| Headline block | left 150, top 268, width 680 | left 60, top 52, width 960 |
| Steps block | left 122, top 536, width 736 | left 478, top 236, width 560, on a cream card (`rgba(251,244,228,.94)`, radius 30, padding 16) |
| Step row | 80 px high, 84 px pitch, one line each | 96 px high, 100 px pitch, text can wrap |
| Step number circle | 52 px | 44 px |
| Phone | left 1030, top 120, 420x860, radius 64 | left 60, top 200, scaled 0.88 |
| Paper note | left 1500, top 300, width 310, rotated -3 deg | left 600, top 820, width 290 |

## Layout per video

| Setting | Cleaner scheduling (v1) | Tax prep (v2) | Backup cleaner (v3) | Door codes (v6) |
|---|---|---|---|---|
| Steps | 3 | 5 | 4 | 4 |
| Wide headline | 72 px, top 268 | 64 px, top 224 | 58 px on 3 lines, top 226 | 62 px on 3 lines |
| Wide step rows | 80 px high, 84 px pitch, 29 px text | 76 px high, 80 px pitch, 23 px text | 84 px high, 88 px pitch, 25 px text | Same as v3 |
| Wide cream panel | about y 206 to 866 | top 190, bottom 880 | top 190, bottom 880 | top 190, bottom 880 |
| Square headline | 56 px | 52 px on 2 lines | 46 px on 2 lines | 46 px on 2 lines |
| Square steps | Cream card to the right of the phone | One row of 5 cards at top 806 | 2x2 grid of cards at top 808 | 2x2 grid of cards |
| Demo surface | Phone | Laptop (database, script card, sample tax form) | Painted room card, tablet calendar, phone | Painted front door with keypad, phone, door codes card |
| Poster frame | 240 (8.0 s) | 264 (8.8 s) | 264 (8.8 s) | 264 (8.8 s) |
| Music track | "Le Croissant" from 76.95 s | "La Pompe Du Trompe" from 87.42 s | "Rendezvous" from 99.12 s | "Parisian" from 0.15 s |

There is no v4 or v5 in this repo. Those numbers are used by videos that are not published here.

The v3 room card uses its own copies of the watercolor filters (`rwc`, `rwc2`, `rgrain`) so the room matches the outdoor scene.

## Painted scene and SVG filters

| Filter | Recipe | Applied to |
|---|---|---|
| `wc` (watercolor edges) | `feTurbulence` fractalNoise, baseFrequency 0.012, numOctaves 3, seed 4, then `feDisplacementMap` scale 22. Filter region -10% / 120%. | Hills, cottage, flowers, grass, cream panel |
| `soft` (billowy clouds) | `feTurbulence` fractalNoise, baseFrequency 0.02, numOctaves 2, seed 9, then `feDisplacementMap` scale 30, then `feGaussianBlur` 2.2 | Clouds and their shadows |
| `grain` (paper texture) | `feTurbulence` fractalNoise, baseFrequency 0.9, numOctaves 2, seed 2, then `feColorMatrix` to a warm brown at 9% alpha | One full-frame rectangle on top |

| Scene part | Detail |
|---|---|
| Clouds | 4 clouds. Start x 300, 1000, 1700, 2400. y 170, 110, 200, 140. Scale 1, 0.7, 1.1, 0.8. Position each frame is `((x0 + t/10*2800) % 2800) - 450`, so they wrap while off screen. |
| Bougainvillea | 3 clusters at (1330, 640), (1830, 620), (1600, 870) with radius 140, 120, 160. 70 circles each, radius 8 to 22 px. A fixed seed places them the same way every frame. |
| Leaves and petals | 9 small ellipses (9 by 4.5 px). Each crosses the frame once per loop and turns twice. |

## Motion

| Curve | Formula | Used for |
|---|---|---|
| Ease in-out (cubic) | `x<.5 ? 4x^3 : 1-(-2x+2)^3/2` | Screen slides, highlight moves, fades |
| Back (overshoot) | `1 + 2.6(x-1)^3 + 1.6(x-1)^2` | Pop-ins (bubble, calendar events, note) |
| Tap ripple | 0.6 s, ring grows from 20 to 100 px and fades | Taps |

## Timeline schema

This table is for the cleaner scheduling video. The beat tables for the other videos are in each video's `script.md`. Each beat is one row. `render(t)` sets every element to its state at time `t`, so there is no hidden state between frames.

| Start (s) | End (s) | Element | Action |
|---|---|---|---|
| 0.0 | 0.6 | Step highlight | On step 1 |
| 0.6 | 1.05 | Text bubble | Pop in (back curve) |
| 0.9 | 1.2 | "Now" label | Fade in |
| 1.7 | 2.3 | Ripple | Tap on link |
| 2.2 | 2.7 | Pick screen | Slide in from right |
| 2.3 | 2.6 | Step highlight | Move to step 2 |
| 3.15 | 3.75 | Ripple | Tap on Sat 6/14 |
| 3.3 | | Sat 6/14 row | Checked |
| 3.95 | 4.55 | Ripple | Tap on Fri 6/20 |
| 4.1 | | Fri 6/20 row | Checked |
| 4.75 | 5.1 | Button | Tap and press to 95% |
| 5.25 | 5.75 | Calendar screen | Slide up |
| 5.35 | 5.65 | Step highlight | Move to step 3 |
| 6.0 | 6.4 | Event on 6/14 | Pop in, entry below slides in (6.1 to 6.5) |
| 6.45 | 6.85 | Event on 6/20 | Pop in, entry below slides in (6.55 to 6.95) |
| 6.9 | 7.35 | Paper note | Pop in |
| 9.0 | 9.6 | Blank thread overlay | Fade in. Note fades out. |
| 9.1 | 9.5 | Step highlight | Back to step 1 |
| 10.0 | | Loop | Matches frame 0 |

## File naming schema

| Pattern | Example | Notes |
|---|---|---|
| `videos/<slug>/` | `videos/schedule-cleaners-by-text/`, `videos/monthly-tax-prep/`, `videos/backup-cleaner-coverage/`, `videos/guest-door-codes/` | One folder per video. The slug is a short kebab-case name based on the title. |
| `<slug>.mp4` | `monthly-tax-prep.mp4` | Main how-to video with music, 1920x1080, 20 s |
| `loop-1920x1080.mp4` | | Silent wide loop, 10 s |
| `loop-1080x1080.mp4` | | Silent square loop, 10 s |
| `poster.png`, `poster-square.png` | | Poster frames from the loops |
| `README.md` | | Title, description, file list, music credit |
| `script.md` | | On-screen script and storyboard |
| `post-run-analysis.md` | | Build notes, checks, fixes, open items |
| `src/v<N>.html` | `src/v2.html` | Scene file for video N (v1 cleaner scheduling, v2 tax prep, v3 backup cleaner, v6 door codes) |
| `src/render-v<N>.sh` | `src/render-v2.sh` | Render script for video N |
| Branch | `videos/<slug>-YYYY-MM-DD` | Usually one pull request per video. The first three videos and the door codes video shared one pull request. |
