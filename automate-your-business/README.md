# Automate Your Business flyers

CURRENT (correct) template: src/template-correct.png (2320x2720)
  = attachment "automate-your-business-workshop.png" on the Sep 25, 2026 email
    "Updated Flyer for Automate Your Business".
  The "event flyer" link in that email goes to Canva: her Canva account (link kept private)
    (editable source; needs Rachael's Canva login)
  (the downloaded email attachment is the same file; only src/template-correct.png is kept in this repo)

Runbook:   PROCESS.md (how to create, check and update these flyers; start here)
Generator: make_flyers_v2.py (see its docstring for usage)
           .venv/bin/python make_flyers_v2.py --session 2026-11-13   (cairosvg lives in that venv)
Schedule:  workshops.json (both series, topics, take-homes)
Logos:     src/logos/ (official XRAY SVGs from Rachael; flyer uses xray-logo-b, the wordmark)
Captions:  captions.md (drafts, not posted)
Outputs:   flyers/flyer-2026-10-30-kiva.png, flyers/flyer-2026-10-09-xray.png and the other 2026 flyers (2320x2720)
           previews/ig-flyer-*.png (1080x1350 Instagram 4:5)
Superseded (wrong template): not included in this repo

## Rebuild from scratch

These steps were run on a fresh clone on Oct 7, 2026, and they rebuilt all six flyers and all six Instagram versions byte for byte.

What you need:
- Python 3 with `venv`. The build used Python 3.13.5.
- The Python packages in `requirements.txt` (numpy, opencv-python-headless, Pillow, CairoSVG), at the versions listed there.
- The cairo library for CairoSVG. On Debian or Ubuntu: `sudo apt install python3-venv libcairo2`. On macOS: `brew install cairo`.
- The fonts Geist and Work Sans. Both are bundled in `fonts/` with their OFL licenses, so you don't need to install them.
- The template `src/template-correct.png` and the logos in `src/logos/`. Both are in this repo.

Commands:

```bash
git clone https://github.com/RachaelQuisel/vacation-rental-automation-how-tos.git
cd vacation-rental-automation-how-tos/automate-your-business
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# Check fonts, schedule data and logos, and test-build every session into scratch/selftest/
.venv/bin/python make_flyers_v2.py --selftest

# Rebuild every 2026 flyer. Full size goes to flyers/, Instagram versions go to previews/
for d in 2026-10-09 2026-10-30 2026-11-13 2026-11-20 2026-12-11 2026-12-18; do
  .venv/bin/python make_flyers_v2.py --session "$d"
done

# If nothing shows as changed, the rebuild matched the committed files
git status --short flyers previews
```

Notes:
- `--selftest` prints "selftest PASSED" at the end. It also prints a note when a heading is scaled down to fit, which is expected for "Office Hours".
- Without CairoSVG, the script falls back to `svgpath_raster.py` for the XRAY logo. That path wasn't checked for a byte-for-byte match, so the logo edges may differ slightly.
- Other package or Python versions will probably work, but the PNGs may not match byte for byte.
- To add a session or change a time, edit `workshops.json` first. `PROCESS.md` has the full runbook.

## Checklist for both flyer sets

This covers the XRAY Office Hours (virtual) set and the Kiva Cowork (in person) set. Both come from the same template and script.

| # | Item | Where |
|---|---|---|
| 1 | Source files and art | `src/template-correct.png` (template), `src/logos/` (XRAY logos), `fonts/` (Geist and Work Sans, OFL). The Kiva icon is cut from the template. |
| 2 | Build scripts, tools and versions | `make_flyers_v2.py`, `svgpath_raster.py`, `requirements.txt`, and "Rebuild from scratch" above |
| 3 | Inputs | `workshops.json` (dates, times, topics, take-homes), `captions.md` (post text) |
| 4 | Step-by-step rebuild | "Rebuild from scratch" above, plus `PROCESS.md` |
| 5 | Design rules | "Design rules" below, `PROCESS.md` sections 2, 3, 6 and 7, and the LAYOUT notes at the top of `make_flyers_v2.py` |
| 6 | Music | None. The flyers are still images with no music. |
| 7 | Finished outputs | `flyers/` (2320x2720) and `previews/` (1080x1350) |
| 8 | Where it was shared | "Where it was shared" below |
| 9 | Field guide | [field-guide.md](field-guide.md) |

## Design rules

- Canvas: 2320x2720 PNG, the size of the template. The Instagram version is cropped to x 51 to 2227 (4:5), then resized to 1080x1350.
- Ink colour: `#0F1A2B`, measured from the template.
- Fonts: Geist for the venue heading, venue lines, date, time and topic. Work Sans for the tagline, agenda, and the AGENDA and TAKE-HOME headers.
- Only the right panel, the agenda, and the take-home rows change between flyers. The script checks that every other pixel matches the template.
- Copy rules (tagline, agenda wording, "worksheet" or "Rulebook", hedged wording) are in `PROCESS.md` section 7.
- The QA checklist is in `PROCESS.md` section 6.

## Where it was shared

- Rachael's Sep 25, 2026 email to the Kiva events contact says she posted that month's flyer (the template flyer for the Fri, Sep 25, 2026 session) on Instagram, LinkedIn, and Facebook. Links: [LINK NEEDED].
- The Oct to Dec 2026 flyers: the captions in `captions.md` are drafts that hadn't been posted as of Oct 7, 2026. The Kiva flyers are attached to email drafts to the Kiva events contact that hadn't been sent as of Oct 7, 2026 (see `kiva-emails.md`).
