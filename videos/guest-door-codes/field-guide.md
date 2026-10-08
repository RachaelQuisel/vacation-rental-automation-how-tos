# Field guide: Door codes for every guest, assigned and revoked automatically

This guide explains every label in the video, how guests, contractors, and the host each see the system, and the questions they're likely to ask. It's based on `script.md`, `../../src/v6.html`, and the other docs in this repo. All names and dates are sample data, and the door codes 4817, 2093 and 6352 are invented sample codes, not codes for any real lock. The video shows how the system is meant to work. Whether it's in use today, and anything the video doesn't show, is To confirm with Rachael.

## Every field and label on screen

**Headline and steps (left panel)**

| On screen | What it means |
|---|---|
| Door codes for every guest, assigned and revoked automatically | The headline |
| 1. A guest books, and the system assigns them a code | A new booking gets its own door code |
| 2. They get their door code in the welcome message, a week before, and a day before their stay | The code is sent three times |
| 3. Every guest and contractor has their own code, so you know who's coming and going | Each person has a separate code, so the entry log shows who came in |
| 4. The code is automatically revoked after checkout and never reused | The code stops working after checkout |

**Painted front door and keypad**

| On screen | What it means |
|---|---|
| LOCKED | The keypad display at rest |
| Keys 1 to 9, *, 0, # | The keypad buttons. No lock brand is shown. |
| Dots on the display | Digits being entered |
| WELCOME, DANA (green) | The code was accepted, and the door opens |
| 4817 REVOKED (red) | That code no longer works |

**Phone: the guest's welcome text**

| On screen | What it means | Where the value comes from |
|---|---|---|
| Dana's phone | Whose phone is shown | |
| La Maison, avatar "LM", Text message | The text comes from the rental's name | The host's business name |
| Mon 6/2 · just booked | Sent when the booking was made | The booking date |
| "Welcome, Dana! Your door code is 4817. Check-in Sun 6/15 after 4 PM." | The guest's first name, their code, and the check-in time | The booking and the assigned code |
| Code sends: At booking (Jun 2), 1 week before (Jun 8), 1 day before (Jun 14), each ticked | The three times the code is sent, and that each one went out | The check-in date |

**"Front door" card**

| On screen | What it means | Where the value comes from |
|---|---|---|
| Front door, June 15 – 18, Sample data | Which door, the dates shown, and a reminder that it's sample data | The lock and the booking |
| New booking · Dana K. · Jun 15–18 | A booking just came in | The booking |
| Checkout · Wed 6/18, 11 AM | The guest's checkout time | The booking |
| Door codes table: name, role (Guest or Cleaner), code, status | Every person with a code | Bookings and the contractor list |
| Active | The code works now | The system |
| Starts 6/18 | The code starts working on that date | The guest's check-in date |
| Revoked (code struck through) | The code no longer works | The system, after checkout |
| Not reused | That code won't be given to anyone else | The system |
| Entry log: role, name, day, date and time | Each time someone used their code | The lock |

**Paper note**: "Codes sent, logged, and revoked ✓". A summary of the result. It isn't part of any app.

## How each person sees it

**The guest (Dana in the sample)**
1. When they book, they get a welcome text from the rental's name with their door code and check-in time.
2. They get the code again a week before and a day before check-in.
3. At the door, they type the code on the keypad. The display greets them by name and the door opens.
4. After checkout, the code stops working.
- When the code starts working (for example, at check-in time or earlier on the check-in day) is To confirm with Rachael.

**A cleaner or other contractor (Maria in the sample)**
- They have their own code, listed as "Cleaner" in the door codes table, and their entries show in the entry log.
- How a contractor gets their code, and whether it's limited to certain days or hours, are To confirm with Rachael.

**The host**
- The "Front door" card shows every active code, who it belongs to, and the entry log.
- After checkout, the guest's code is marked Revoked and Not reused.
- Which lock and app the real system uses isn't shown. To confirm with Rachael.

## FAQ

**Guest: When will I get my door code?**
In the video, at booking, a week before, and a day before check-in, by text.

**Guest: Can I get in before check-in time?**
The video doesn't show this. To confirm with Rachael.

**Guest: What if my code doesn't work?**
The video doesn't show this case. To confirm with Rachael.

**Guest: Will my code work after I check out?**
No. The video shows the code revoked after checkout.

**Cleaner: Do I share a code with the guest?**
No. In the video, every guest and contractor has their own code.

**Host: Can I see who came in and when?**
Yes. The entry log lists each entry with the person's role, name, and time.

**Host: Could an old code be given to a new guest?**
The video shows revoked codes marked "Not reused".

**Anyone: Are these real codes?**
No. 4817, 2093 and 6352 are invented sample codes, and the names are made up.
