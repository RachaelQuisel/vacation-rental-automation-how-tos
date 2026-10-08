# Field guide: Automate Your Business flyers

This guide covers every label and value printed on the flyers, both the XRAY Office Hours (virtual) set and the Kiva Cowork (in person) set. It also covers how each person involved sees them, and gives a short FAQ. It's based on `make_flyers_v2.py`, `workshops.json`, `PROCESS.md`, `captions.md`, and `events.md`.

## Every field on the flyer

Left column (the same on every flyer):

| On the flyer | What it means | Where the value comes from |
|---|---|---|
| AUTOMATE YOUR BUSINESS | The workshop name | Printed in the template |
| MONTHLY HANDS-ON BUSINESS AUTOMATION WORKSHOP | What kind of event it is | Printed in the template |
| WITH / Rachael Quisel / AI and Automation Workflow Consultant at XRAY | Who leads the workshop | Printed in the template |
| AGENDA: Hands-on demo, Q & A, Leave with a tangible solution | What happens in the hour | `AGENDA` in `make_flyers_v2.py`. You can override it with `--agenda`. |
| TAKE-HOME | The header for what attendees leave with | `TK_LABEL` in the script. You can override it with `--takehome-label`. |
| Take-home line, for example "Your Loop Audit worksheet" | The worksheet or page attendees take home for that topic | `takehome` for the session's topic in `workshops.json` |
| FREE • DROP IN | The workshop costs nothing, and you can come without signing up | Printed in the template |

Right panel (changes per flyer):

| On the flyer | What it means | Where the value comes from |
|---|---|---|
| Logo or icon left of the heading | The gold hex icon means Kiva Cowork. The "XRAY" wordmark means XRAY Office Hours. | `preset` for the series in `workshops.json`. The Kiva icon is cut from the template, and the XRAY wordmark is `src/logos/xray-logo-b-6c8bc69c.svg`. |
| Venue heading: "Kiva Cowork" or "Office Hours" | Where or how the session happens | Kiva: from the template. XRAY: the `xray` preset in the script. |
| Venue lines: "1117 State St, Santa Barbara" and "Upstairs Conference Room", or "Virtual, join from anywhere" | The address for the in-person sessions, or a note that the virtual sessions are online | Kiva: from the template. XRAY: the `xray` preset in the script. |
| DATE AND TIME | Header for the date and time | Printed in the template |
| Date, for example "FRI, OCT 30" | The session day | `flyer_date` for the session in `workshops.json`. The selftest checks that it matches the ISO `date`. |
| Time, for example "2:30 PM" or "9 AM PT" | The start time | `flyer_time` for the session in `workshops.json`. The full start and end times are in `start` and `end`. |
| Topic, for example "The Loop Audit" | That session's workshop topic | `name` for the session's topic in `workshops.json` |
| Tagline: "Take your workflow from messy idea to a system that works." | The workshop promise, in Rachael's words | `TAGLINE` in the script. You can override it with `--tagline`. |
| Photo | Rachael | Printed in the template |

The flyers have no QR code, link, email address, or phone number. The virtual join link isn't printed on the flyer. In the captions it shows as `[JOIN LINK NEEDED]` until Rachael adds it.

## How each person sees it

**Someone thinking of attending (in person, Kiva Cowork)**
- They might see the flyer on Instagram, in a Kiva member email, or around the space. Kiva said on Sep 25, 2026 that it would include the workshop in member announcements.
- The flyer tells them the day, start time, topic, address, and room, and that it's free and drop-in. The full time is 2:30 to 3:30 PM PT. The flyer prints only the start time.
- They don't need to register. They walk in at the time on the flyer and go upstairs to the conference room.

**Someone thinking of attending (virtual, XRAY Office Hours)**
- They'd see the flyer on Instagram or other social posts.
- The flyer tells them the day, "9 AM PT", the topic, and that it's online. The full time is 9 to 10 AM PT.
- They need a join link, which isn't on the flyer. How they get it is To confirm with Rachael.

**Kiva Cowork (the venue)**
- Rachael emails the Kiva events contact the full-size flyer, named like `automate-your-business-oct-30.png`, with the date, time and room. She asks for it to go to the member list a week before and the day before (see `kiva-emails.md`).

**Rachael (the host)**
- She edits `workshops.json`, runs the script, checks each flyer at full size, and approves every post and email before it goes out. See `PROCESS.md`.

## FAQ

**Do I need to sign up?**
The flyer says FREE • DROP IN, so for the in-person sessions you can just come. For the virtual sessions, how to get the join link is To confirm with Rachael.

**Does it cost anything?**
No. The flyer says FREE.

**How long is it?**
About 60 minutes. Kiva sessions run 2:30 to 3:30 PM PT, and XRAY sessions run 9 to 10 AM PT.

**Do I need to be a Kiva member?**
Kiva said on Sep 25, 2026 that the workshop is open to the public.

**What should I bring?**
The captions suggest bringing one recurring task you'd like to untangle. Whether a laptop is needed is To confirm with Rachael.

**What's the take-home?**
It depends on the topic: a Loop Audit worksheet, a Colleague Audit worksheet, or a one-page Rulebook. It's printed on each flyer.

**Why are the November and December Kiva dates different?**
They moved a week early for the holidays, to Nov 20 and Dec 18, 2026, instead of the last Friday.

**Is the virtual session the same as the in-person one?**
Both series teach the same three topics in the same order. Each month the virtual session comes first, and the Kiva session follows one to three weeks later.

**Will there be food?**
The Kiva captions mention snacks. The virtual sessions don't.
