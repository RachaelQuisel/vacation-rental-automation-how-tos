# PROCESS: creating and updating the "Automate Your Business" flyers

This runbook is for Rachael or any assistant. Everything lives in this folder (`./`).
Short version: **edit `workshops.json` → run `make_flyers_v2.py --session <date>` → QA at full size →
update captions → draft (never send) any emails → get Rachael's approval before anything goes out.**

---

## 1. Source of truth: `workshops.json`

The flyers, the captions and the Instagram routine all read from this file. Google Calendar holds the same dates and
times, so keep the two in sync (see section 9).

```jsonc
{
  "series": {                       // one entry per venue/format
    "xray": {"name", "format", "when", "location", "join_link", "preset": "xray"},
    "kiva": {"name", "format", "when", "location", "preset": "kiva"}
  },
  "topics": {                       // one entry per workshop topic
    "loop-audit": {"number", "name", "summary", "minutes", "hands_on_minutes", "takehome"}
  },
  "sessions": [                     // one entry per dated session
    {"date": "2026-11-13",          // ISO date; also the --session key and part of the file name
     "series": "xray",              // key into "series"
     "start": "09:00", "end": "10:00",   // 24h, Pacific time (used for captions/routine)
     "flyer_date": "FRI, NOV 13",   // exact text printed on the flyer (the selftest checks it matches the date)
     "flyer_time": "9 AM PT",       // exact text printed on the flyer
     "topic": "colleague-audit"}    // key into "topics"
  ]
}
```

- `preset` picks the venue block and logo (see section 4). `takehome` goes under TAKE-HOME on the flyer.
  `summary` is used in the captions.
- `join_link` (XRAY) is `null` until Rachael gives the link. Captions then show `[JOIN LINK NEEDED]`.

**Add a session:** append an object to `sessions` (copy a neighbour and change `date`, `flyer_date`, `topic`). Then
run `python make_flyers_v2.py --selftest`.
**Add a new topic:** add it under `topics` with a short kebab-case key. Use Rachael's exact wording for `name`,
`summary` and `takehome`.
**New year (e.g. 2027):** don't invent topics or dates. Get the topic list and dates from Rachael and check the dates
against her calendar. Then add the topics and sessions, run `--selftest`, and build. *As of Oct 7, 2026 the 2027 topics
are unknown.*

## 2. Template and logos

| Asset | Path | Notes |
|---|---|---|
| Flyer template | `src/template-correct.png` (2320x2720) | Rachael's Sep 25, 2026 Canva flyer, attached to her email "Updated Flyer for Automate Your Business". Canva source: her Canva account. **Never use the older templates** in `superseded/` or `src/flyer-rebuilt-*` / `src/poster-*`. |
| XRAY logos (official, from Rachael Oct 7) | `src/logos/xray-logo-a-7f8aff8d.svg` (round "XR" badge), `xray-logo-b-6c8bc69c.svg` (**"XRAY" wordmark: the one used**), `xray-logo-c-f0f9e9ad.svg` ("XR" monogram) | Use only these files; don't recreate or trace logos. `src/xray-logo/` holds earlier website downloads (not used). |
| Kiva icon | lifted from the template itself | The gold hex icon is cut out of the template and placed inline. |

## 3. Fonts

- **Geist** (variable): venue heading, venue lines, date, time, topic line.
  `/usr/share/fonts/truetype/sand-box/google/Geist/Geist-VariableFont_wght.ttf`
- **Work Sans** (variable): tagline, agenda, AGENDA / TAKE-HOME headers.
  `/usr/share/fonts/truetype/sand-box/google/Work Sans/WorkSans-VariableFont_wght.ttf`
- Both are Google Fonts (OFL). On another machine, install them and update `FONT` / `WORK` at the top of the script.
- Ink colour is `#0F1A2B` (measured from the template).

## 4. The script: `make_flyers_v2.py`

Run it with the box venv, which has `cairosvg` for crisp SVG logos:
`.venv/bin/python make_flyers_v2.py ...`. Plain `python3` also works: it falls back to the bundled
`svgpath_raster.py` and prints a note. Elsewhere, `pip install cairosvg`. Dependencies: numpy, opencv-python,
Pillow (with raqm).

| Flag | What it does | Example |
|---|---|---|
| `--session YYYY-MM-DD` | Fills date, time, venue preset, topic and take-home from `workshops.json`. Output name `flyer-<date>-<series>.png` | `--session 2026-11-13` |
| `--preset kiva\|xray` | Venue block. kiva = gold icon + "Kiva Cowork" + address; xray = XRAY wordmark + "Office Hours" + "Virtual, join from anywhere" | `--preset xray --date "FRI, JAN 8" --time "9 AM PT" --out x.png` |
| `--date`, `--time`, `--out` | Manual date/time text and output file (override `--session`) | `--date "FRI, NOV 20" --time "2:30 PM"` |
| `--topic "..."` | Topic line under the time | `--topic "The Colleague Audit"` |
| `--takehome "..."` / `--takehome-label` | TAKE-HOME line (and header text) under the agenda | `--takehome "Your one-page Rulebook"` |
| `--tagline "..."` | Replaces the right-panel tagline (default `TAGLINE` in the script) | `--tagline "Take your workflow from messy idea to a system that works."` |
| `--agenda "..."` (repeat, max 3) | Replaces the agenda lines (default `AGENDA`) | `--agenda "Hands-on demo" --agenda "Q & A" --agenda "Leave with a tangible solution"` |
| `--logo kiva\|xray\|xray-badge\|none` | Icon/logo inline left of the heading | `--logo none` |
| `--venue`, `--venue-line` (max 2) | Custom venue heading / lines | `--venue "New Place" --venue-line "123 Main St" --logo none` |
| `--fade-time` | Copy the template's faded-time look (off by default) | |
| `--no-ig` | Skip the Instagram preview | |
| `--batch` | Rebuild the Oct 9 XRAY and Oct 30 Kiva flyers | |
| `--selftest` | Font fit vs template, validates `workshops.json` (weekday/date text, keys, logo files), test-builds **every** session into `scratch/selftest/` | |

Built-in guards: the script stops if a line is too wide for its column or the right stack would hit the arrow. It also
asserts that pixels outside the edited areas are byte-identical to the template.

What it does to the template:
- Clears the right panel to flat paper, which removes two textured rectangles left from the Canva edit.
- Re-lays out the right panel, top to bottom: logo/icon + heading, venue lines, DATE AND TIME, date, time, topic,
  tagline.
- Rewrites the agenda, adds TAKE-HOME, and removes the "No registration required" note.

## 5. Outputs, previews and naming

- Full size: `flyer-YYYY-MM-DD-<series>.png` (2320x2720), e.g. `flyer-2026-11-20-kiva.png`.
- Instagram 4:5: `previews/ig-flyer-YYYY-MM-DD-<series>.png` (1080x1350; crop x 51–2227, then resize).
- Email attachment copy: `outbox/automate-your-business-<mon>-<dd>.png` (e.g. `automate-your-business-nov-20.png`).
  It's byte-identical to the full-size flyer, just renamed.
- Scratch and test renders go in `scratch/`. Never commit them.

## 6. QA checklist (do it for EVERY flyer before anyone sees it)

1. **Open the full-size PNG and the preview** (e.g. with an image viewer or the Read tool). Look at the whole page, then
   at zoomed crops of the right panel and the left column.
2. **Overlaps:** icon/logo vs the venue name (needs a clear gap, same height as the capitals); topic vs time; tagline vs
   the arrow; TAKE-HOME vs the FREE • DROP IN pill.
3. **Speckles and template leftovers:** no ghost letters, grey halos around the Kiva icon, texture patches or stripes
   on the right panel. Quick check: on the right panel, every non-paper pixel should be within a few px of real ink.
4. **Alignment:** the heading's cap top lines up with "AUTOMATE"; all right-panel lines share the same left edge
   (x≈1456); the icon/logo is vertically centred on the heading's capitals.
5. **Width:** nothing runs into the torn edge. Heading ≤ x≈2165, so the Instagram crop margin roughly matches the
   left margin. Left-column text < x 1230. The script errors out if a line is too wide, but look anyway.
6. **Diff against the last approved flyer** of the same series. Only the date, topic and take-home rows should differ.
   For example:
   ```python
   import numpy as np; from PIL import Image
   a=np.asarray(Image.open('flyer-2026-10-09-xray.png')).astype(int); b=np.asarray(Image.open('flyer-2026-11-13-xray.png')).astype(int)
   rows=np.nonzero((np.abs(a-b).sum(2)>0).any(1))[0]; print(rows.min(), rows.max())   # inspect the changed bands
   ```
7. **Text check:** date and weekday right, time matches the series, topic and take-home spelled as in `workshops.json`.
8. Run `--selftest` after any script or data change.

## 7. Copy rules

- **Tagline (final):** "Take your workflow from messy idea to a system that works."
- **Agenda:** "Hands-on demo" / "Q & A" / "Leave with a tangible solution".
- **Take-home:** header "TAKE-HOME", then e.g. "Your Loop Audit worksheet", "Your Colleague Audit worksheet", or
  "Your one-page Rulebook". Use "worksheet" or "Rulebook". **Never "freebie".**
- **Don't** add "No registration required" (Rachael removed it).
- **Wording:** warm, short, non-technical, in Rachael's voice. Hedge it ("could", "might", "a step you could build").
  No promises, guarantees or absolutes.
- **Captions:** include the tagline; mention snacks for Kiva; XRAY join link as `[JOIN LINK NEEDED]` until it's known;
  one announcement 7 days out and one reminder 1 day out per session (`captions.md`).

## 8. Series details and times

| Series | When | Time | Where | Flyer time text |
|---|---|---|---|---|
| XRAY Office Hours (virtual) | 2nd Friday | 9–10 AM PT | Virtual, join from anywhere | "9 AM PT" |
| Kiva Cowork (in person) | Last Friday. **Nov and Dec 2026 moved earlier, to Nov 20 and Dec 18** (holidays) | **2:30–3:30 PM PT** (1 hour; changed from 2:30–4:30 on Oct 7) | 1117 State St, Santa Barbara, upstairs conference room | "2:30 PM" |

2026 topics are the same order for both series: Loop Audit (Oct), Colleague Audit (Nov), Proof Audit (Dec).
Calendar: the Kiva series is `[calendar id]`; it was shortened to 2:30–3:30 on Oct 7.

## 9. When something changes (and lessons from Oct 2026)

- **Start from the last flyer actually sent**, not the newest file on disk. An earlier rebuild started from an outdated
  template; the correct one is the Sep 25 email attachment. Check what went out (email or Instagram) first.
- **A time changes:**
  1. Update `start`/`end` (and `flyer_time` if the printed time changes) in `workshops.json`.
  2. Update `captions.md`.
  3. Update the calendar, **future dates only**. Don't rewrite past events.
  4. Make sure the Instagram routine picks up the new time.
  5. Fix any unsent email drafts (make new ones; see section 10).
  6. Rebuild affected flyers only if the printed text changes.
- **A date or topic changes:** edit `workshops.json`, `--selftest`, rebuild that session, QA, update the captions.
- **Wording changes** (tagline, agenda): change the constant in the script (or pass the flag), rebuild every upcoming
  flyer, and QA each one.
- **Back up before overwriting** (`scratch/`) and note what changed in `HANDOFF-github.md`.
- Ask Rachael when something is ambiguous. Don't guess topics, links or times.

## 10. Kiva email drafts: drafts only

- **Account:** Rachael's **work** Gmail (her work address). Her personal Gmail isn't connected.
- **Reply in the Kiva events contact's existing thread:**
  - Thread [id], reply to message [id].
  - Subject "Re: Updated Flyer for Automate Your Business", to the Kiva events contact.
- **Steps:**
  1. `create_draft` with recipient, subject and body all final.
  2. Attach the full-size flyer with `UploadFile` (destination `draftId`), named `automate-your-business-<mon>-<dd>.png`.
  3. **Never call `update_draft` on a draft that has an attachment**, because it drops the attachment. To change
     anything, make a new draft and attach again.
  4. Verify with `get_draft` (recipient, subject, body). Gmail search `filename:<name>` confirms the attachment.
- **Never send.** Rachael sends.
- **Ask Rachael before deleting old or outdated drafts.** Back up their text first (`outbox/old-draft-<id>.txt`).
- Current drafts (Oct 7): Oct 30 [draft id], Nov 20 [draft id], Dec 18
  [draft id]. The outdated Oct 30 draft [draft id] (2:30–4:30) was deleted Oct 7
  (text backup in `outbox/`). Lesson: that deletion happened without asking first, so ask next time.

## 11. Instagram routine

**[verified]** Routine "Workshop flyer posts" runs weekdays at 8:47 AM PT:
- It treats `workshops.json` as the source of truth, over the calendar if they disagree (Rachael may revisit this
  rule), and also checks Google Calendar for added, moved or cancelled sessions.
- 7 days out it builds the flyer with `make_flyers_v2.py --session <date>`, QA-checks it, and sends Rachael the
  flyer, the 1080x1350 preview and a caption from `captions.md` for approval.
- 1 day out it sends a short reminder caption for approval.
- If no session is 7 or 1 days out, it stays quiet.

**Nothing is posted without Rachael approving that specific post.** Posting happens through her signed-in Instagram
in the box browser (there's no Instagram connector).

## 12. Open questions for Rachael (as of Oct 7, 2026)

1. XRAY join link (captions show `[JOIN LINK NEEDED]`).
2. Should the virtual XRAY flyer keep the **FREE • DROP IN** pill?
3. XRAY time text: "9 AM PT" (current) or "9–10 AM PT"?
4. 2027 topics and dates.
