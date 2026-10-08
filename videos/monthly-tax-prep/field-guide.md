# Field guide: Monthly TOT and TBID tax prep

This guide explains every label in the video, how the host (and anyone who helps with the books) sees the system, and the questions they're likely to ask. It's based on `script.md`, `../../src/v2.html`, and the other docs in this repo. All bookings, amounts, and the account number are sample data. The video shows how the system is meant to work. Where the real system's behavior isn't shown or written down, this guide says To confirm with Rachael.

TOT is the transient occupancy tax, and TBID is the tourism business improvement district assessment.

## Every field and label on screen

**Headline and steps (left panel)**

| On screen | What it means |
|---|---|
| Monthly tax prep, done before you sit down | The headline |
| 1. Your platforms are connected to track payouts and charges | Booking platforms send their payouts and fees in |
| 2. Income and expenses are added to a database | Every payout and fee becomes a row |
| 3. A script calculates your TOT and TBID | The tax math runs on the month's income |
| 4. A script maps the numbers onto the official tax form | The results fill the city's form |
| 5. An audit script checks that the numbers add up | A second script rechecks the totals |

**Laptop screen 1: Tax prep database**

| On screen | What it means | Where the value comes from |
|---|---|---|
| June, Sample data (tags) | The month being prepared, and a reminder that the numbers are made up | The filing month |
| Airbnb, Vrbo, "Connecting" then "Payouts + charges" with a green dot | Each booking platform is connected and sending data | The host's platform accounts |
| Date | When the payout or charge happened | The platform record |
| Source | Which platform it came from | The platform record |
| Type: Income or Expense | Rent paid to the host, or a fee taken out | The platform record |
| Item, for example "Rent, 3 nights" or "Host service fee" | What the row is for | The platform record |
| Amount, for example $1,410.00 or -$42.30 | The amount. Fees show as negative. | The platform record |
| Income $10,240.00, Expenses $307.20, 18 rows | The month's totals | Added up from all rows |

**Laptop screen 2: Script card**

| On screen | What it means |
|---|---|
| tax_calc · June, "running" then "done ✓" | The calculation script for the month, and whether it has finished |
| taxable_rent = income | Taxable rent is the month's rent income |
| TOT = 10,240.00 × 12% | TOT at 12% |
| TBID = 10,240.00 × 2% | TBID at 2% |
| total_due = TOT + TBID | The total to pay |

The 12% and 2% rates were taken from the city's website on Oct 7, 2026. Please confirm current rates before relying on them.

**Laptop screen 3: Sample tax form**

| On screen | What it means | Where the value comes from |
|---|---|---|
| City of Santa Barbara, TOT & TBID Monthly Return | A simplified sample of the city's monthly form | The form layout |
| Sample, invented numbers (tag) | The numbers are made up | Fixed label |
| Filing period: June | The month being filed | The filing month |
| Business name: La Maison | The rental's business name | The host's account details |
| TOT account: SAMPLE-0001 | The city tax account number. The video uses a placeholder. | The host's account details |
| 1. Total rents for the month | All rent for the month | Database income |
| 2a. Stays over 30 days, 2b. Federal or diplomat stays | Rent that may be exempt | Rows marked as exempt. All $0.00 in the sample. |
| 3. Taxable rents | Line 1 minus lines 2a and 2b | Calculated |
| 4. TOT due (12%) | TOT owed | The script |
| 5. Room rental revenue, 6a, 6b, 7. Taxable rents | The same steps for TBID | Database income and the script |
| 8. TBID due (2%) | TBID owed | The script |
| 9. Total TOT + TBID due | The amount to pay | Line 4 plus line 8 |
| Audit bar: "Line 1 = database income · 12% and 2% rechecked · Line 9 = 4 + 8", then "Totals match ✓" | What the audit script checked, and that it passed | The audit script |
| Green ticks next to lines 1, 3, 4, 5, 7, 8, and 9 | Each checked line | The audit script |

**Paper note**: "June return, totals checked ✓". A summary of the result. It isn't part of any app.

## How each person sees it

**The host**
- They see the month's rows and totals in the database, the calculation result, and a filled form with each line checked.
- Whether the host submits the form themselves or the system submits it isn't shown in the video. To confirm with Rachael.
- How exempt stays (over 30 days, or federal or diplomat) get marked is To confirm with Rachael.

**A bookkeeper or accountant**
- They can follow each form line back to a database total, and see which lines the audit script checked.
- How they get access to the database or the filled form is To confirm with Rachael.

There are no cleaners or guests in this workflow.

## FAQ

**Host: Does this file my taxes for me?**
The video shows the form being filled and checked. Who submits it is To confirm with Rachael.

**Host: Are the rates right for my city?**
The video uses Santa Barbara's 12% TOT and 2% TBID as of Oct 7, 2026. Other cities and later dates may differ, so please check with your city.

**Host: What if a platform fee is charged in a different month?**
The video doesn't show this case. To confirm with Rachael.

**Host: Why is taxable rent the same as income in the sample?**
The sample has no exempt stays, so lines 2a, 2b, 6a and 6b are all $0.00.

**Bookkeeper: How do I know the totals are right?**
The audit script rechecks that line 1 matches database income, recomputes 12% and 2%, and checks that line 9 equals line 4 plus line 8. It shows "Totals match ✓" when they agree.

**Host: Is the account number real?**
No. "SAMPLE-0001" and all the amounts are made up.
