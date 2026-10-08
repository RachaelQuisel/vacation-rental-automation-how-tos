# Workflow diagrams

## Production pipeline

```mermaid
flowchart TD
    A["Plan: headline, numbered steps, sample data"] --> B["Build the HTML scene<br/>painted SVG + phone screens + render(t)"]
    B --> C["Capture frames with headless Chrome<br/>30 fps, 300 frames per 10 s loop"]
    C --> D1["Wide frames 1920x1080"]
    C --> D2["Square frames 1080x1080 (?sq)"]
    D1 --> E1["ffmpeg encode<br/>loop-1920x1080.mp4"]
    D2 --> E2["ffmpeg encode<br/>loop-1080x1080.mp4"]
    D1 --> P["Poster frames<br/>frame 240 = 8.0 s"]
    D2 --> P
    E1 --> Q["QC: pull still frames and look at each one"]
    E2 --> Q
    Q --> R{"Any problems?<br/>clipped text, overlaps, typos, real data"}
    R -- "Yes" --> B
    R -- "No" --> M["Music version<br/>loop twice + 20 s track excerpt + loudnorm"]
    M --> C2["Add the CC BY credit line"]
    C2 --> V["Owner review"]
    P --> V
    V --> G["Pull request to this repo"]
    G --> H["Owner merges"]
```

## The 10 second loops

Each video is a 10 second loop. These diagrams show the beats in order. Times are seconds into the loop.

### Schedule your cleaners by text

```mermaid
sequenceDiagram
    participant S as Steps panel
    participant P as Cleaner phone
    participant C as Shared calendar
    Note over S,P: 0.0 s, step 1 is on, empty text thread
    P->>P: 0.6 s, text message pops in
    P->>P: 1.7 s, tap on the link
    P->>P: 2.2 s, Pick your dates slides in
    S->>S: 2.3 s, highlight moves to step 2
    P->>P: 3.15 s, tap Sat 6/14
    P->>P: 3.95 s, tap Fri 6/20
    P->>C: 4.75 s, tap Sign me up
    C->>C: 5.25 s, shared calendar slides up
    S->>S: 5.35 s, highlight moves to step 3
    C->>C: 6.0 s, Maria added to 6/14
    C->>C: 6.45 s, Maria added to 6/20
    Note over C: 6.9 s, paper note pops in
    Note over S,C: 8.0 s, poster frame
    Note over S,C: 9.0 to 9.6 s, blank thread fades in, back to step 1
```

### Monthly TOT and TBID tax prep

```mermaid
sequenceDiagram
    participant S as Steps panel
    participant D as Tax prep database
    participant X as Script card
    participant F as Sample tax form
    Note over S,D: 0.25 s, Airbnb and Vrbo connect
    D->>D: 0.75 to 2.3 s, six sample rows land
    S->>S: 1.9 s, highlight moves to step 2
    D->>D: 2.3 to 3.1 s, totals count up
    S->>S: 3.3 s, highlight moves to step 3
    D->>X: 3.4 s, script card rises
    X->>X: 3.75 to 4.75 s, TOT and TBID calculated
    S->>S: 4.95 s, highlight moves to step 4
    X->>F: 5.05 s, form slides up
    F->>F: 5.8 s, lines fill in
    S->>S: 7.25 s, highlight moves to step 5
    F->>F: 7.35 s, audit bar checks the lines
    Note over F: 8.3 s, Totals match
    Note over S,F: 8.8 s, poster frame
    Note over S,F: 9.0 to 9.6 s, opening screen fades back in
```

### When your cleaner can't make it, the next one is asked automatically

```mermaid
sequenceDiagram
    participant S as Steps panel
    participant R as Guest room
    participant C as Cleaning calendar
    participant P as Phone
    Note over R: 0.05 to 1.2 s, messy room and dismayed guests
    R->>C: 2.1 s, room shrinks, calendar and tasks appear
    S->>S: 3.2 s, highlight moves to step 2
    C->>P: 3.4 s, Maria gets the invite
    S->>S: 4.3 s, highlight moves to step 3
    P->>C: 4.45 s, Maria declines
    C->>P: 5.05 s, Rosa gets the invite
    P->>C: 5.8 s, Rosa accepts
    C->>R: 6.25 to 7.4 s, room is cleaned
    S->>S: 7.6 s, highlight moves to step 4
    C->>P: 8.05 s, text alert for the open Saturday
    Note over S,P: 8.8 s, poster frame
    Note over S,P: 9.0 to 9.6 s, empty calendar fades back in
```

### Door codes for every guest, assigned and revoked automatically

```mermaid
sequenceDiagram
    participant S as Steps panel
    participant K as Front door and keypad
    participant P as Guest phone
    participant T as Door codes card
    Note over S,T: 0.35 s, new booking for a sample guest
    T->>T: 0.7 to 1.6 s, a sample code rolls in
    S->>S: 2.1 s, step 2, phone slides up at 2.2 s
    T->>P: 2.7 s, welcome text with the code
    P->>P: 3.05 to 4.1 s, three code sends ticked
    S->>S: 4.45 s, step 3, guest at the door at 4.55 s
    P->>K: 4.95 to 5.55 s, guest types the code
    K->>T: 5.9 s, entry logged
    T->>T: 6.25 s, other sample codes and entries appear
    S->>S: 7.1 s, step 4, checkout at 7.2 s
    T->>K: 7.45 to 7.8 s, code revoked on the card and the keypad
    Note over S,T: 8.8 s, poster frame
    Note over S,T: 9.0 to 9.6 s, opening card fades back in
```

### When an inspection finds a problem, the right contractor is scheduled automatically

```mermaid
sequenceDiagram
    participant S as Steps panel
    participant I as Inspector phone
    participant C as Contractor phone
    participant T as Team chat and cards
    Note over S,T: 0.0 s, step 1 is on, checklist at 0 of 6
    I->>I: 0.35 to 1.15 s, three items ticked
    I->>I: 1.6 to 1.72 s, kitchen sink flagged with a note
    S->>S: step 2, sheet slides up at 2.4 s
    I->>C: 3.05 to 3.65 s, tap Send to plumber, the text flies over
    C->>C: 3.68 to 4.18 s, job text and three time slots
    S->>S: step 3
    C->>I: 5.2 to 5.65 s, contractor taps the next open time and replies
    S->>S: step 4
    T->>I: 6.9 s, confirmation banner on the inspector phone
    T->>C: 7.08 s, confirmation text to the contractor
    T->>T: 7.25 to 7.85 s, text card, email card, and maintenance post
    Note over S,T: 8.3 s, paper note. 8.8 s, poster frame
    Note over S,T: 9.0 to 9.6 s, opening screens fade back in
```
