# Script and storyboard: Monthly TOT and TBID tax prep

This is the on-screen script for the 10 second loop. The music version plays the same loop twice (20 seconds) with a music track. There is no voiceover and no caption line.

All bookings, amounts, and account numbers are sample data. The tax rates shown (12% TOT and 2% TBID) were taken from the city's website during the build on Oct 7, 2026. They have not been rechecked since, so please confirm current rates before relying on them.

## Headline

> Monthly tax prep, done before you sit down

## Numbered steps

1. Your platforms are connected to track payouts and charges
2. Income and expenses are added to a database
3. A script calculates your TOT and TBID
4. A script maps the numbers onto the official tax form
5. An audit script checks that the numbers add up

The highlight on the steps moves in sync with the laptop demo.

## Laptop screens

**Tax prep database** (tags "June" and "Sample data")

- Two connected sources, "Airbnb" and "Vrbo" (plain text, no logos). Each goes from "Connecting" to "Payouts + charges".
- Six of 18 sample rows (Date, Source, Type, Item, Amount):
  - Jun 3, Airbnb, Income, Rent, 3 nights, $1,410.00
  - Jun 3, Airbnb, Expense, Host service fee, -$42.30
  - Jun 8, Vrbo, Income, Rent, 4 nights, $1,920.00
  - Jun 8, Vrbo, Expense, Payment processing, -$57.60
  - Jun 14, Airbnb, Income, Rent, 2 nights, $980.00
  - Jun 14, Airbnb, Expense, Host service fee, -$29.40
- Footer totals: Income $10,240.00, Expenses $307.20, 18 rows.

**Script card** ("tax_calc · June", status "running" then "done ✓")

```
taxable_rent = income        $10,240.00
TOT  = 10,240.00 × 12%        $1,228.80
TBID = 10,240.00 × 2%           $204.80
total_due = TOT + TBID        $1,433.60
```

**Sample tax form** ("City of Santa Barbara, TOT & TBID Monthly Return", tag "Sample, invented numbers")

- Filing period: June. Business name: La Maison. TOT account: SAMPLE-0001.
- Lines 1, 3, 5, and 7: $10,240.00. Lines 2a, 2b, 6a, and 6b: $0.00.
- Line 4 (TOT due, 12%): $1,228.80. Line 8 (TBID due, 2%): $204.80. Line 9 (total due): $1,433.60.
- Audit bar: "Line 1 = database income · 12% and 2% rechecked · Line 9 = 4 + 8", then "Totals match ✓".

**Paper note** (handwritten style, taped on)

> June return, totals checked ✓

## Beats

| Time (s) | Step shown | What happens |
|---|---|---|
| 0.25 to 0.9 | 1 | Airbnb, then Vrbo, go from "Connecting" to a green dot. |
| 0.75 to 2.3 | 1 | Six rows fly out of their source card into the database, one every 0.22 s. Each source card glows as its row leaves. |
| 1.9 to 2.2 | 1 to 2 | The highlight moves to step 2. |
| 2.3 to 3.1 | 2 | The footer counts up Income, Expenses, and rows. |
| 3.3 to 3.6 | 2 to 3 | The highlight moves to step 3. |
| 3.4 to 3.75 | 3 | The dark script card rises. Its four lines type in from 3.75 s. |
| 4.75 | 3 | The script status changes to "done ✓". |
| 4.95 to 5.25 | 3 to 4 | The highlight moves to step 4. |
| 5.05 to 5.5 | 4 | The sample tax form slides up. Lines fill in from 5.8 s, one every 0.12 s. |
| 7.25 to 7.55 | 4 to 5 | The highlight moves to step 5. |
| 7.35 to 7.7 | 5 | The audit bar slides in. Green ticks pop next to lines 1, 3, 4, 5, 7, 8, and 9 from 7.65 s. |
| 8.3 | 5 | "Totals match ✓" lights up. |
| 8.45 to 8.85 | 5 | The paper note pops in. |
| 8.8 | 5 | Poster frame. |
| 9.0 to 9.6 | 5 to 1 | A copy of the opening screen fades in, and the note fades out. The highlight returns to step 1 at 9.1 to 9.5. |
| 10.0 | 1 | Loop point. |

## Audio (music version only)

- Track: "La Pompe Du Trompe" by Shane Ivers, a gypsy jazz piece.
- Excerpt: 87.42 s to 107.42 s of the track, chosen to start on a bar downbeat.
- 0.3 s fade in, 1.5 s fade out (18.5 s to 20.0 s), leveled to about -16 LUFS.
- Credit (required, CC BY 4.0): Music: "La Pompe Du Trompe" by Shane Ivers ([silvermansound.com](https://www.silvermansound.com)), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- Source page: https://www.silvermansound.com/free-music/la-pompe-du-trompe
