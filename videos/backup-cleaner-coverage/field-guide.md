# Field guide: When your cleaner can't make it, the next one is asked automatically

This guide explains every label in the video, how the cleaners and the host each see the system, and the questions they're likely to ask. It's based on `script.md`, `../../src/v3.html`, and the other docs in this repo. All names, dates, and messages are sample data. The video shows how the system is meant to work. Where the real system's behavior isn't shown or written down, this guide says To confirm with Rachael.

## Every field and label on screen

**Headline and steps (left panel)**

| On screen | What it means |
|---|---|
| When your cleaner can't make it, the next one is asked automatically | The headline |
| 1. Each booking creates a cleaning task | A new stay adds a turnover to the cleaning calendar |
| 2. Your cleaner gets a calendar invite | The first cleaner is invited to that turnover |
| 3. If they decline, it goes to the next cleaner | A decline sends the invite to the next cleaner |
| 4. You get a text if a day still needs coverage | The host is alerted when nobody has accepted |

**Painted room card**

| On screen | What it means |
|---|---|
| Thu 6/19 · 4 PM check-in | The next guests arrive at 4 PM, so the room has to be clean by then |
| Ready for 4 PM check-in ✓ | The turnover is done |

**Tablet: Cleaning calendar**

| On screen | What it means | Where the value comes from |
|---|---|---|
| Cleaning calendar, June 15 – 21, Sample data | One week of the calendar, with a reminder that it's sample data | The host's calendar |
| Sun 15 to Sat 21 | The days of the week | The calendar |
| Stays row, "Stay, 2 nights" | Guest stays from bookings | Bookings |
| Turnovers row, 11 AM to 3 PM | A cleaning task for each turnover, with its cleaning window | Created from each booking |
| New task | A turnover was just created and nobody has been invited yet | The booking |
| Maria G., Invite sent | An invite went to that cleaner, and there's no reply yet | The system, using the cleaner order |
| Maria G. (struck through), Declined | That cleaner said no | The cleaner's reply to the invite |
| Rosa P., Invite sent, then Accepted ✓ | The next cleaner was invited and said yes | The system, then the cleaner's reply |
| Asking cleaners | Invites are going out for that day | The system |
| Needs a cleaner, dashed outline, "!" badge | Nobody has accepted that turnover yet | The system |
| Footer, for example "4 turnovers · 3 have a cleaner · Sat still open" | A summary of the week | Counted from the turnovers |

**Phone: the cleaner's calendar invite**

| On screen | What it means |
|---|---|
| Maria's phone, Rosa's phone | Whose phone is shown |
| Calendar invite | It arrives as a calendar invite |
| Turnover at La Maison | The event title, with the rental's name |
| Thu, Jun 19 | The turnover date |
| 11 AM – 3 PM | The cleaning window |
| From: cleaning schedule | Who sent the invite |
| Decline, Accept | The cleaner's two choices |
| Declined, Accepted ✓ (stamps) | The reply was recorded |

**Phone: the host's text alert**

| On screen | What it means |
|---|---|
| Your phone | The host's phone |
| Alerts, Text message, bell icon | A text alert from the system. No phone number is shown. |
| Today 9:30 AM | When the alert arrived |
| "Heads up: Sat 6/21 turnover still needs a cleaner." | The day that still has no cleaner |

**Paper note**: "Declined invite, rerouted to Rosa ✓". A summary of the result. It isn't part of any app.

## How each person sees it

**The first cleaner (Maria in the sample)**
1. They get a calendar invite titled "Turnover at La Maison" with the date and the 11 AM to 3 PM window, from "cleaning schedule".
2. They tap Decline if they can't make it, or Accept if they can.
3. If they decline, the turnover goes to the next cleaner.
- Which calendar app the invite opens in, and whether the cleaner also gets a text, are To confirm with Rachael.

**The next cleaner (Rosa in the sample)**
1. They get the same invite after the first cleaner declines.
2. They tap Accept, and the turnover shows their name on the calendar.

**The host**
- The cleaning calendar shows each turnover's status: New task, Invite sent, Declined, Accepted, Asking cleaners, or Needs a cleaner.
- If a day still has no cleaner, the host gets a text alert naming the day.
- How the order of cleaners is set, how long the system waits for a reply before moving on, and when the alert is sent (the sample shows 9:30 AM) are To confirm with Rachael.

## FAQ

**Cleaner: What happens if I decline?**
The invite goes to the next cleaner. You don't have to find a replacement yourself.

**Cleaner: What happens if I don't reply at all?**
The video doesn't show this case. To confirm with Rachael.

**Cleaner: Can I change my answer after I accept?**
The video doesn't show this case. To confirm with Rachael.

**Cleaner: What are the hours?**
The invite shows the cleaning window, 11 AM to 3 PM in the sample, between checkout and the 4 PM check-in.

**Host: How will I know if nobody can clean?**
The day shows "Needs a cleaner" on the calendar, and you get a text like "Heads up: Sat 6/21 turnover still needs a cleaner."

**Host: Where do the cleaning tasks come from?**
Each booking creates a cleaning task on the calendar.

**Host: Are these real cleaners?**
No. Maria G., Rosa P., and the dates are made-up sample data.
