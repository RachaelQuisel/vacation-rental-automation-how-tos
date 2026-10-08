---
name: workshop-flyers
description: Create, update, and QA recurring event/workshop flyers that are generated from a fixed image template plus a schedule data file (e.g. Rachael Quisel's "Automate Your Business" flyers in this folder). Use when asked to make flyers for new or future sessions, change a date, time, topic, tagline, agenda, take-home or logo on existing flyers, write the matching Instagram captions, or prepare (never send) email drafts that carry a flyer.
---

# Workshop flyers

## When to use
- Someone needs a flyer for an upcoming session, or a batch of future flyers.
- A session's date, time, topic, venue or wording changed and the flyers, captions or drafts must follow.
- Captions or venue emails need to go with a flyer.

## Where things live (Automate Your Business instance)
- Project folder: `./` (this folder). Read `PROCESS.md` there first: it's the full runbook.
- Data: `workshops.json` (series → preset, topics → name/summary/take-home, sessions → date, flyer text, topic).
- Template: `src/template-correct.png`. Logos: `src/logos/`. Fonts: Geist + Work Sans.
- Generator: `make_flyers_v2.py`. Run it with `.venv/bin/python` (a venv with cairosvg).
- Outputs: `flyer-YYYY-MM-DD-<series>.png` + `previews/ig-…` (1080x1350). Email copies in `outbox/`.
- Captions: `captions.md`. Handoff/changelog: `HANDOFF-github.md`.

## Workflow
1. **Confirm the facts.** Dates and times come from the data file and the owner's calendar. Topics, links and wording
   come from the owner. Never invent missing ones; use a placeholder like `[JOIN LINK NEEDED]` and list it as an open
   question.
2. **Start from the last flyer actually sent/approved** and the correct template. Check what really went out before
   rebuilding.
3. **Edit the data file**, not the image: add or change sessions/topics, then run `--selftest`.
4. **Build:** `--session YYYY-MM-DD` per flyer (or flags for one-offs: `--preset`, `--date`, `--time`, `--topic`,
   `--takehome`, `--tagline`, `--agenda`, `--logo`).
5. **QA every output at full size and in the preview:**
   - overlaps (icon/logo vs heading, text vs arrow, take-home vs pill)
   - stray specks, halos or template leftovers
   - left-edge alignment and cap-top alignment
   - text fits inside its column and the Instagram crop margins
   - diff against the last approved flyer of the same series: only the intended rows should change
   - spelling of date, weekday, time, topic and take-home
6. **Captions:** one 7-days-out announcement and one 1-day-out reminder per session. Short and warm, in the owner's
   voice, with the tagline. Hedged wording; no promises or absolutes. Venue-specific details (e.g. snacks at the
   in-person venue).
7. **Emails with a flyer:** create the draft as a reply in the existing thread (`create_draft` with recipient, subject
   and body final), then attach with `UploadFile` (draftId). Never `update_draft` a draft with an attachment; make a
   new one instead. Verify with `get_draft`. **Never send.** Ask before deleting old drafts, and back them up first.
8. **Record the change** in the handoff/changelog. Keep a backup of anything overwritten.

## When something changes
- Time change: update the data file, the captions, the calendar (future dates only), the posting routine and any
  unsent drafts (as new drafts). Rebuild flyers only if the printed text changes.
- Wording change: update the script default or pass the flag, then rebuild and QA every upcoming flyer.
- New year: get topics and dates from the owner first. Then add them to the data file, `--selftest`, build, QA.

## Hard rules
- Nothing is posted, sent or deleted without the owner's explicit approval of that specific action.
- Use only official logo files supplied by the owner. Never recreate a logo.
- No secrets or tokens in any committed file.
