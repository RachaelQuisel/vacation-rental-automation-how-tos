#!/usr/bin/env python3
"""
make_flyers_v2.py: generate "Automate Your Business" flyers from the CORRECT template.

TEMPLATE
  src/template-correct.png, 2320x2720 flat PNG. This is the "automate-your-business-workshop.png"
  attachment on Rachael's Sep 25, 2026 email "Updated Flyer for Automate Your Business". It is byte-identical to the image she sent on Oct 7.
  The editable source is her Canva design: her Canva account (link kept private)
  (needs her Canva login; not used here).

QUICK START
  # one session from the schedule (date, time, venue, topic, take-home all come from workshops.json)
  .venv/bin/python make_flyers_v2.py --session 2026-11-13
  # rebuild the Oct 9 (XRAY) and Oct 30 (Kiva) flyers
  .venv/bin/python make_flyers_v2.py --batch
  # checks: font fit, schedule data, and a test build of every session into scratch/selftest/
  .venv/bin/python make_flyers_v2.py --selftest
  The venv is only needed for cairosvg, which renders the official XRAY logo SVG. Plain python3 works
  too (the bundled svgpath_raster.py takes over and prints a note), or run `pip install cairosvg`.
  Every run also writes an Instagram 4:5 copy (1080x1350) to previews/ig-<outname>
  (crop x 51..2227, then resize). Use --no-ig to skip it.

SCHEDULE DATA: workshops.json
  series (xray, kiva) -> preset; topics (loop-audit, colleague-audit, proof-audit) -> name,
  summary, minutes, hands-on minutes, take-home; sessions -> ISO date, series, start/end,
  flyer_date, flyer_time, topic. Google Calendar is the source of truth for dates and times.
  Keep the file in sync with it.

LAYOUT (round 3, Oct 7, 2026)
  Right panel, top to bottom. The heading's cap top is aligned with the cap top of "AUTOMATE" (y=213):
    [icon/logo] Venue heading     Kiva: gold hex icon, ~cap height, left of "Kiva Cowork"
                                  XRAY: official XRAY wordmark (src/logos/xray-logo-b-6c8bc69c.svg)
                                        at exactly cap height, left of "Office Hours"
    venue line(s)                 Kiva: 2 address lines; XRAY: "Virtual, join from anywhere"
    DATE AND TIME / date / time   template spacing (label +159.5, date +116.5, time +224 px)
    topic line                    e.g. "The Loop Audit" (Geist 560, 56 px)
    tagline                       TAGLINE, Work Sans 430 53 px, 3-4 balanced lines
  The template's right panel is flat paper except two textured rectangles (with dark ragged left
  edges) that the Canva edit left behind the venue and date blocks. RP_BOX is cleared to flat paper
  (242,241,237) and the stack is laid out again. Original Canva text that doesn't change (Kiva
  heading and address, the "DATE AND TIME" label) and the Kiva icon are lifted out as alpha and
  moved, not retyped. The icon is scaled to ~1.08x cap height.
  Left column: AGENDA = "Hands-on demo" / "Q & A" / "Leave with a tangible solution";
  optional TAKE-HOME header + line (e.g. "Your Loop Audit worksheet"); the "No registration
  required" note under the FREE • DROP IN pill is removed (the pill stays).
  Pixels outside the edit boxes stay byte-identical (asserted). The template's typefaces are Geist
  (venue, date, time) and Work Sans (tagline, agenda, headers).

MANUAL USE (flags override --session values)
  python3 make_flyers_v2.py --preset kiva --date "FRI, NOV 20" --time "2:30 PM" \
      --topic "The Colleague Audit" --takehome "Your Colleague Audit worksheet" --out x.png
  --venue/--venue-line replace the venue block; --logo kiva|xray|xray-badge|none;
  --tagline, --agenda (repeat), --takehome-label, --fade-time (copy the template's faded time).

NOTES
  * Venue headings that are too wide are scaled down to fit (logo included): "Office Hours" next
    to the XRAY wordmark comes out at 83 px; "Kiva Cowork" stays at 99 px.
  * The tagline only shrinks (max 3%) if it needs to for a clean wrap with no weak word
    ("the", "to", ...) at a line end.
  * The script errors out if the right stack would run into the arrow or a left-column line is
    too wide.
  * xray-badge (round "XR" badge, logo a) was tried and rejected: its letters get tiny at cap height.
"""
import argparse, os, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, 'src', 'template-correct.png')
def _font_path(env, file, system):
    # Font lookup order: an environment variable, then fonts/ next to this script (bundled in the
    # repo), then the system path used on the original build machine.
    if os.environ.get(env): return os.environ[env]
    local = os.path.join(HERE, 'fonts', file)
    return local if os.path.exists(local) else system

FONT = _font_path('FLYER_FONT_GEIST', 'Geist-VariableFont_wght.ttf',
                  '/usr/share/fonts/truetype/sand-box/google/Geist/Geist-VariableFont_wght.ttf')
INK = np.array([15, 26, 43], float)          # #0F1A2B, measured from the template
S = 4                                        # supersampling factor
RIGHT_LIMIT = 2250                           # text must end before this x (torn-paper panel)
HEAD_MAX_W = 2165 - 1456                     # venue heading may run as far right as the address lines do

# Calibrated against the template (pen origin = left/baseline, in template px)
STY = {
    'head':  dict(size=99, wght=690, track=-2.1),
    'line':  dict(size=56, wght=400, track=0.2),
    'date':  dict(size=99.25, wght=800, track=-3.1),
}
X0 = 1456.25                                 # left edge of the Canva text boxes (same for every line)
POS = {
    'head': (X0, 423.5), 'line1': (X0, 520.0), 'line2': (X0, 596.0),
    'date': (X0, 872.0), 'time': (X0, 979.5),
}
LOGO_BOX = (185, 330, 1440, 1600)            # y0,y1,x0,x1 around the gold hex logo
VENUE_BOX = (335, 625, 1440, 2250)           # heading + two address lines
DT_BOX = (785, 1000, 1440, 2250)             # date + time lines
IG_CROP = (51, 0, 2227, 2720)                # 2176x2720 = 4:5

PRESETS = {
    'kiva': dict(venue=None, lines=None, logo='kiva'),
    # official XRAY wordmark (says "XRAY") sits inline left of the heading, so the heading is "Office Hours"
    'xray': dict(venue='Office Hours', lines=['Virtual, join from anywhere'], logo='xray'),
}

def _font(size, wght, path=None):
    f = ImageFont.truetype(path or FONT, int(round(size * S)))
    f.set_variation_by_axes([wght])
    f._wght = (wght,)
    return f

def _width(s, st, min_gap_em=0.22):
    f = _font(st['size'], st['wght'], st.get('font'))
    xs = _layout(s, f, st['size'], st['track'], min_gap_em)
    e = _ink_extent(f, s[-1])
    return (xs[-1] + (e[1] if e else 0)) / S

def _fill(img, m):
    """Fill masked pixels from the surrounding paper using multi-scale normalized convolution.
    That reproduces the paper's soft mottling without the streaks/specks of cv2.inpaint."""
    img = img.astype(np.float32); W = (1 - m).astype(np.float32)
    out = img.copy(); done = W > 0
    for sig in (3, 6, 12, 24, 48, 96):
        num = cv2.GaussianBlur(img * W[..., None], (0, 0), sig)
        den = cv2.GaussianBlur(W, (0, 0), sig)[..., None]
        ok = (den[..., 0] > 0.25) & ~done
        est = num / np.maximum(den, 1e-6)
        out[ok] = est[ok]; done |= ok
        if done.all(): break
    return out

def erase(arr, box, kind='ink', seed=0):
    """Remove text (dark ink) or the logo (gold) inside box and refill with paper."""
    y0, y1, x0, x1 = box
    band = arr[y0:y1, x0:x1].copy()
    f = band.astype(int)
    if kind == 'ink':
        bgsum = np.median(f.sum(2))           # paper ~720 (stripe ~685), yellow ~494; ink ~84
        m = f.sum(2) < bgsum - 60
    else:                                     # gold logo: R noticeably above B
        m = (f[..., 0] - f[..., 2]) > 9
    m = cv2.dilate(m.astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
    out = _fill(band, m)
    # paper grain: the template background has ~0.3 level of fine noise
    # (the flat yellow has none, so only add grain where the surrounding background has it)
    hf = band.astype(np.float32) - cv2.GaussianBlur(band.astype(np.float32), (0, 0), 2)
    far = cv2.dilate(m, np.ones((31, 31), np.uint8)) == 0      # background well away from text
    sig = min(0.35, float(hf[far].std())) if far.any() else 0.0
    if sig > 0.05:
        out += np.random.default_rng(seed).normal(0, sig, out.shape[:2])[..., None]
    a = cv2.GaussianBlur(m.astype(np.float32), (0, 0), 1.0)[..., None]   # feather edge
    a = np.maximum(a, m[..., None])
    res = band.astype(np.float32) * (1 - a) + out * a
    arr[y0:y1, x0:x1] = res.round().clip(0, 255).astype(np.uint8)
    return m.sum()

_INK_CACHE = {}
def _ink_extent(f, ch):
    """(left, right) ink extent of ch relative to its pen x, in supersampled px."""
    k = (f.size, f.getname(), tuple(round(v) for v in f._wght), ch)
    if k not in _INK_CACHE:
        sz = f.size * 3
        m = Image.new('L', (sz, sz), 0); ImageDraw.Draw(m).text((sz // 3, sz * 2 // 3), ch, font=f, fill=255, anchor='ls')
        cols = np.nonzero((np.asarray(m) > 100).any(0))[0]
        _INK_CACHE[k] = (cols.min() - sz // 3, cols.max() - sz // 3) if len(cols) else None
    return _INK_CACHE[k]

def _layout(s, f, size, track, min_gap_em):
    """Pen x for each char (supersampled px, relative to origin). Uses the font's kerning plus
    the template tracking. Word gaps that come out visibly tighter than the template's
    (e.g. 'Y O' in 'XRAY Office') are opened up to min_gap_em * size."""
    xs = []; extra = 0.0
    for i, ch in enumerate(s):
        x = f.getlength(s[:i]) + i * track * S + extra
        if ch == ' ' and 0 < i < len(s) - 1 and min_gap_em:
            a, b = _ink_extent(f, s[i - 1]), _ink_extent(f, s[i + 1])
            if a and b:
                prev_x = xs[i - 1]
                nxt_x = f.getlength(s[:i + 1]) + (i + 1) * track * S + extra
                gap = (nxt_x + b[0]) - (prev_x + a[1])
                need = min_gap_em * size * S
                if gap < need: extra += need - gap
        xs.append(x)
    return xs

MIN_GAP = {'head': 0.20, 'line': 0.27, 'date': 0.21}

def draw(arr, s, pos, size, wght, track, fade=False, min_gap_em=0.22, font=None):
    x, y = pos
    f = _font(size, wght, font)
    pad = int(size * 0.6)
    X0, Y0 = int(x) - pad, int(y) - int(size * 1.1)
    W = int(f.getlength(s) / S + abs(track) * len(s) + size) + 2 * pad
    W = min(W, arr.shape[1] - X0)
    H = int(size * 1.5)
    m = Image.new('L', (W * S, H * S), 0); d = ImageDraw.Draw(m)
    for ch, px in zip(s, _layout(s, f, size, track, min_gap_em)):
        d.text(((x - X0) * S + px, (y - Y0) * S), ch, font=f, fill=255, anchor='ls')
    a = np.asarray(m.resize((W, H), Image.LANCZOS), float)[..., None] / 255.0
    cols = np.nonzero((a[..., 0] > 0.1).any(0))[0]
    if len(cols) and X0 + cols.max() >= RIGHT_LIMIT:
        raise SystemExit(f'Text too wide for the panel: {s!r}')
    ink = np.broadcast_to(INK, a.shape[:2] + (3,)).copy()
    if fade:   # copy the template's bottom fade on the time line (last ~30 px get lighter)
        rows = np.arange(H) + Y0
        t = ((rows - (y - 30)) / 30).clip(0, 1) ** 1.6
        ink = ink + (np.array([65, 73, 86.]) - INK) * t[:, None, None]
    reg = arr[Y0:Y0 + H, X0:X0 + W].astype(float)
    arr[Y0:Y0 + H, X0:X0 + W] = (reg * (1 - a) + ink * a).round().clip(0, 255).astype(np.uint8)

# ---- Template edits applied to EVERY flyer (Rachael, Oct 7, 2026) ---------------------------
WORK = _font_path('FLYER_FONT_WORKSANS', 'WorkSans-VariableFont_wght.ttf',
                  '/usr/share/fonts/truetype/sand-box/google/Work Sans/WorkSans-VariableFont_wght.ttf')
# 1. Right-panel blurb -> her tagline (Work Sans, same size, style and line pitch as the old blurb)
TAGLINE = 'Take your workflow from messy idea to a system that works.'   # Rachael, Oct 7 (final)
TAG_STY = dict(size=53, wght=430, track=-0.5, font=WORK)
TAG_X, TAG_BASE0, TAG_PITCH = 1455.0, 1144.0, 83.0
TAG_MAX_W = 2180 - 1455                      # old blurb's widest line ended at x=2152
TAG_BOX = (1090, 1440, 1440, 2250)
# 2. Agenda (Oct 7 round 2): exactly three lines, in the template's three agenda slots
AGENDA = ['Hands-on demo', 'Q & A', 'Leave with a tangible solution']
AG_STY = dict(size=53, wght=420, track=1.2, font=WORK)
AG_X, AG_BASE0, AG_PITCH = 120.5, 1802.0, 98.0
AG_BOX = (1745, 2030, 100, 1240)
# 3. Remove 'No registration required' under the pill (pill stays)
NOTE_BOX = (2510, 2585, 140, 900)
# Optional take-home block under the agenda (off unless takehome= / --takehome is given):
# a header in the AGENDA/WITH header style + one line in the agenda style.
HDR_STY = dict(size=51, wght=700, track=0.0, font=WORK)   # fitted to 'AGENDA'
TK_LABEL = 'TAKE-HOME'
TK_HDR_BASE = 1998.0 + 120.0                 # last agenda baseline + a section gap
TK_LINE_BASE = TK_HDR_BASE + 95.0            # same header->item spacing as AGENDA (1707 -> 1802)
TK_BOX = (2030, 2300, 100, 1240)
LEFT_MAX_X = 1230                            # left-column text must end before the torn edge

WEAK_END = {'a', 'an', 'the', 'i', 'to', 'of', 'from', 'and', 'or', 'how', 'lay', 'where', 'between'}

def _wrap(text, st, maxw, nmin=3, nmax=4):
    """Balanced wrap into 3-4 lines. Returns (weak_count, lines) for the most even split that fits,
    avoiding lines that end on a word leaning on the next one ('the', 'an', 'lay' [out] ...)."""
    import itertools
    words = text.split(); best = None
    cache = {}
    def w(t):
        if t not in cache: cache[t] = _width(t, st, 0.27)
        return cache[t]
    for n in range(nmin, nmax + 1):
        for cuts in itertools.combinations(range(1, len(words)), n - 1):
            ls = [' '.join(words[a:b]) for a, b in zip((0,) + cuts, cuts + (len(words),))]
            ws = [w(l) for l in ls]
            if max(ws) > maxw: continue
            weak = sum(l.split()[-1].lower() in WEAK_END for l in ls[:-1])
            cost = (weak, sum((maxw - x) ** 2 for x in ws[:-1]) + (0 if ws[-1] > 0.4 * maxw else 1e9))
            if best is None or cost < best[0]: best = (cost, ls)
    return (best[0][0], best[1]) if best else (99, None)

def fit_tagline(text, st, maxw, max_shrink=0.03):
    """Natural size first; shrink by at most 3% only if that's needed for a clean wrap."""
    size0 = st['size']; fallback = None; size = size0
    while size >= size0 * (1 - max_shrink) - 1e-6:
        weak, ls = _wrap(text, dict(st, size=size), maxw)
        if ls and fallback is None: fallback = (size, ls)
        if ls and weak == 0: return size, ls
        size = round(size - 0.5, 2)
    if fallback: return fallback
    size = size0
    while size > 36:                         # last resort: shrink until it fits at all
        size -= 0.5
        weak, ls = _wrap(text, dict(st, size=size), maxw)
        if ls: return size, ls
    raise SystemExit('tagline does not fit')

def left_column(arr, boxes, agenda=None, takehome=None, takehome_label=None):
    """Left (yellow) column: agenda lines, optional TAKE-HOME block, remove the pill note."""
    agenda = list(agenda or AGENDA)
    if len(agenda) > 3: raise SystemExit('At most 3 agenda lines fit above the pill')
    erase(arr, AG_BOX, 'ink', 5); boxes.append(AG_BOX)
    for i, l in enumerate(agenda):
        if AG_X + _width(l, AG_STY, 0.27) > LEFT_MAX_X: raise SystemExit(f'Agenda line too wide: {l!r}')
        draw(arr, l, (AG_X, AG_BASE0 + i * AG_PITCH), min_gap_em=0.27, **AG_STY)
    if takehome:
        shift = (len(agenda) - 3) * AG_PITCH         # sits a section gap below the last agenda line
        lbl = (takehome_label or TK_LABEL).upper()
        if AG_X + _width(takehome, AG_STY, 0.27) > LEFT_MAX_X: raise SystemExit(f'Take-home line too wide: {takehome!r}')
        draw(arr, lbl, (AG_X - 1.0, TK_HDR_BASE + shift), min_gap_em=0.2, **HDR_STY)
        draw(arr, takehome, (AG_X, TK_LINE_BASE + shift), min_gap_em=0.27, **AG_STY)
        boxes.append(TK_BOX)
    erase(arr, NOTE_BOX, 'ink', 6); boxes.append(NOTE_BOX)

# ---- Right panel (round 3, Oct 7): re-laid out on clean paper -------------------------------
# The template's right panel is flat paper (242,241,237) except two textured rectangles that her
# Canva edit pasted behind the venue block and the date block (with dark ragged left edges). The
# script clears that region back to flat paper and lays the stack out again. Original Canva text
# that stays the same (Kiva heading/address, DATE AND TIME) is moved as-is (alpha pixels), not
# re-typed.
PAPER = np.array([242, 241, 237], np.uint8)
RP_BOX = (85, 1500, 1405, 2265)              # cleared region (arrow starts below y=1539 here)
TOP_CAP = 213                                # heading cap top = cap top of "AUTOMATE" on the left
HEAD_CAP = 71.5                              # cap height of the 99px venue heading (352 -> 423.5)
# vertical rhythm measured from the template (baseline to baseline)
D_HEAD_LINE1, D_LINE, D_LINE_LABEL = 96.5, 76.0, 159.5
D_LABEL_DATE, D_LABEL_TIME, D_TIME_TAG = 116.5, 224.0, 164.5
TOPIC_STY = dict(size=56, wght=560, track=0.2)     # Geist, address-line size, a bit heavier
D_TIME_TOPIC, D_TOPIC_TAG = 92.0, 150.0
ICON_GAP_EM = 0.24                           # icon/logo -> heading gap, in heading-size ems
KIVA_ICON_SCALE = 1.08                       # Kiva hex height = 1.08 x cap height (thin linework)
# Official XRAY logos sent by Rachael (Oct 7), in src/logos/: a = round "XR" badge, b = "XRAY"
# wordmark, c = "XR" monogram. The flyer uses the wordmark (b) inline left of "Office Hours".
XRAY_LOGOS = {'xray': os.path.join(HERE, 'src', 'logos', 'xray-logo-b-6c8bc69c.svg'),
              'xray-badge': os.path.join(HERE, 'src', 'logos', 'xray-logo-a-7f8aff8d.svg')}
BADGE_SCALE = 1.25                           # badge height / cap height (round mark looks smaller)

def render_logo(path, height_px):
    """Rasterize an SVG logo at an exact pixel height -> alpha array. Uses cairosvg (install with
    `pip install cairosvg`, or run this script with .venv/bin/python); falls back
    to the bundled svgpath_raster for simple path-only SVGs."""
    try:
        import cairosvg, io
        svg = open(path).read().replace('currentColor', '#000000')
        png = cairosvg.svg2png(bytestring=svg.encode(), output_height=height_px)
        return np.asarray(Image.open(io.BytesIO(png)).convert('RGBA'), np.float32)[..., 3] / 255
    except ImportError:
        from svgpath_raster import render_svg
        print('  (cairosvg not installed: using the bundled SVG path rasterizer)')
        return render_svg(path, height_px)[0]
# boxes of original Canva elements in the template (y0,y1,x0,x1) and their baselines
ORIG = {'head': ((340, 440, 1440, 2100), 423.5), 'line1': ((470, 545, 1440, 2200), 520.0),
        'line2': ((545, 620, 1440, 2200), 596.0), 'label': ((705, 770, 1440, 2100), 755.5)}

def _ink_alpha(src, box):
    """Alpha of dark ink inside box, measured against the (textured) paper behind it."""
    y0, y1, x0, x1 = box
    band = src[y0:y1, x0:x1]
    s = band.astype(np.float32).sum(2)
    m = cv2.dilate((s < np.median(s) - 60).astype(np.uint8), np.ones((9, 9), np.uint8))
    bg = _fill(band, m).sum(2)
    a = ((bg - s) / np.maximum(bg - INK.sum(), 1)).clip(0, 1)
    return np.where(a < 0.04, 0, a)          # drop residue of the old texture

def _kiva_icon_rgba(src):
    y0, y1, x0, x1 = LOGO_BOX
    band = src[y0:y1, x0:x1].astype(np.float32)
    gold = (band[..., 0] - band[..., 2]) > 9
    m = cv2.dilate(gold.astype(np.uint8), np.ones((7, 7), np.uint8))
    bg = _fill(band, m)
    # alpha from the blue channel (gold absorbs blue; the paper does not)
    coreB = np.percentile(band[..., 2][gold], 5)          # bluest-poor = fully opaque gold
    a = ((bg[..., 2] - band[..., 2]) / np.maximum(bg[..., 2] - coreB, 1)).clip(0, 1) * (m > 0)
    a = np.where(a < 0.15, 0, a)                          # paper-texture residue -> transparent
    # stroke colour: taken from the solid core pixels, spread smoothly to the soft edges
    solid = (a > 0.7).astype(np.float32)
    k = (0, 0)
    num = cv2.GaussianBlur(band * solid[..., None], k, 3); den = cv2.GaussianBlur(solid, k, 3)
    col = num / np.maximum(den, 1e-3)[..., None]
    ys, xs = np.nonzero(a > 0.02)
    sl = (slice(ys.min(), ys.max() + 1), slice(xs.min(), xs.max() + 1))
    return a[sl], col[sl].clip(0, 255)

def _paste(arr, alpha, color, x, y):
    """Composite alpha (HxW) in color (rgb or HxWx3) with top-left at integer (x, y)."""
    h, w = alpha.shape; a = alpha[..., None]
    reg = arr[y:y + h, x:x + w].astype(np.float32)
    c = np.broadcast_to(np.asarray(color, np.float32), (h, w, 3))
    arr[y:y + h, x:x + w] = (reg * (1 - a) + c * a).round().clip(0, 255).astype(np.uint8)

def _resize_alpha(alpha, h):
    w = max(1, round(alpha.shape[1] * h / alpha.shape[0]))
    return np.asarray(Image.fromarray((alpha * 255).astype(np.uint8)).resize((w, h), Image.LANCZOS), np.float32) / 255

def right_panel(arr, src, date, time, venue=None, lines=None, logo='kiva', topic=None,
                tagline=None, fade_time=False):
    """venue=None keeps the Kiva heading + address (moved as-is). logo: 'kiva' | 'xray' | None."""
    # 1) grab the original pieces we keep, then clear the panel to flat paper
    keep = {k: _ink_alpha(src, b) for k, (b, _) in ORIG.items()}
    kicon = _kiva_icon_rgba(src) if logo == 'kiva' else None
    y0, y1, x0, x1 = RP_BOX
    arr[y0:y1, x0:x1] = PAPER
    head_base = TOP_CAP + HEAD_CAP
    # 2) heading line: [icon/logo] + heading
    if venue is None:                                     # Kiva: original heading, moved
        hb, hbase = ORIG['head']
        xshift = 0
        if logo == 'kiva':
            a, col = kicon
            h = round(HEAD_CAP * KIVA_ICON_SCALE)
            ar = _resize_alpha(a, h)
            colr = cv2.resize(col, (ar.shape[1], h), interpolation=cv2.INTER_AREA)
            _paste(arr, ar, colr, round(X0), round(TOP_CAP + HEAD_CAP / 2 - h / 2))
            xshift = ar.shape[1] + round(ICON_GAP_EM * 99)
        _paste(arr, keep['head'], INK, hb[2] + xshift, round(hb[0] + head_base - hbase))
        nlines = 2
        for i in (1, 2):
            b, base = ORIG['line%d' % i]
            _paste(arr, keep['line%d' % i], INK, b[2], round(b[0] + head_base + D_HEAD_LINE1 + (i - 1) * D_LINE - base))
    else:
        lines = list(lines or []); nlines = len(lines)
        hs = dict(STY['head'])
        aspect = {'xray': 492.2 / 146, 'xray-badge': BADGE_SCALE}.get(logo, 0)
        lw = lambda st: (_width(venue, st, MIN_GAP['head']) +
                         (aspect * 0.722 * st['size'] + ICON_GAP_EM * st['size'] if aspect else 0))
        while lw(hs) > HEAD_MAX_W and hs['size'] > 60:
            hs['size'] -= 1
        if hs['size'] != STY['head']['size']:
            print(f'  heading shrunk to {hs["size"]}px (template 99px) to fit the panel')
        cap = 0.722 * hs['size']                          # Geist cap height
        hbase = TOP_CAP + cap
        x = X0
        if logo == 'xray':                                # wordmark letters = exactly cap height
            la = render_logo(XRAY_LOGOS[logo], round(cap))
            _paste(arr, la, INK, round(X0), round(TOP_CAP))
            x = X0 + la.shape[1] + ICON_GAP_EM * hs['size']
        elif logo == 'xray-badge':                        # round badge, centred on the cap height
            h = round(cap * BADGE_SCALE)
            la = render_logo(XRAY_LOGOS[logo], h)
            _paste(arr, la, INK, round(X0), round(TOP_CAP + cap / 2 - h / 2))
            x = X0 + la.shape[1] + ICON_GAP_EM * hs['size']
        draw(arr, venue, (x, hbase), min_gap_em=MIN_GAP['head'], **hs)
        head_base = hbase
        for i, ln in enumerate(lines):
            draw(arr, ln, (X0, head_base + D_HEAD_LINE1 + i * D_LINE), min_gap_em=MIN_GAP['line'], **STY['line'])
    last = head_base + D_HEAD_LINE1 + (max(nlines, 1) - 1) * D_LINE
    # 3) DATE AND TIME label (original, moved), date, time
    lb, lbase = ORIG['label']
    label_base = last + D_LINE_LABEL
    _paste(arr, keep['label'], INK, lb[2], round(lb[0] + label_base - lbase))
    draw(arr, date, (X0, label_base + D_LABEL_DATE), min_gap_em=MIN_GAP['date'], **STY['date'])
    time_base = label_base + D_LABEL_TIME
    draw(arr, time, (X0, time_base), fade=fade_time, min_gap_em=MIN_GAP['date'], **STY['date'])
    # 4) optional topic line under the time, then the tagline
    if topic:
        tb = time_base + D_TIME_TOPIC
        draw(arr, topic, (X0, tb), min_gap_em=MIN_GAP['line'], **TOPIC_STY)
        tag0 = tb + D_TOPIC_TAG
    else:
        tag0 = time_base + D_TIME_TAG
    st = dict(TAG_STY)
    size, ls = fit_tagline(tagline or TAGLINE, st, TAG_MAX_W)
    fnt = st.pop('font')
    for i, l in enumerate(ls):
        draw(arr, l, (TAG_X, tag0 + i * TAG_PITCH), size=size, wght=st['wght'],
             track=st['track'], min_gap_em=0.27, font=fnt)
    if tag0 + (len(ls) - 1) * TAG_PITCH + 20 > RP_BOX[1]:
        raise SystemExit('right panel stack runs into the arrow')
    return ls

def build(out, date, time, venue=None, lines=None, no_logo=False, fade_time=False, ig=True,
          tagline=None, agenda=None, takehome=None, takehome_label=None,
          topic=None, logo=None):
    src = np.array(Image.open(TEMPLATE).convert('RGB'))
    arr = src.copy()
    boxes = [RP_BOX]
    left_column(arr, boxes, agenda, takehome, takehome_label)
    if logo is None:
        logo = None if no_logo else 'kiva'
    right_panel(arr, src, date, time, venue, lines, logo, topic, tagline, fade_time)
    # integrity check: nothing outside the edited boxes changed
    keep = np.ones(arr.shape[:2], bool)
    for y0, y1, x0, x1 in boxes: keep[y0:y1, x0:x1] = False
    assert (arr[keep] == src[keep]).all(), 'pixels outside edit boxes changed'
    if not os.path.isabs(out):
        # a bare file name goes in flyers/, where the repo keeps the full-size flyers
        out = os.path.join(HERE, 'flyers', out) if not os.path.dirname(out) else os.path.join(HERE, out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    Image.fromarray(arr).save(out, optimize=True)
    print('saved', out)
    if ig:
        os.makedirs(os.path.join(HERE, 'previews'), exist_ok=True)
        igp = os.path.join(HERE, 'previews', 'ig-' + os.path.basename(out))
        Image.fromarray(arr).crop(IG_CROP).resize((1080, 1350), Image.LANCZOS).save(igp, optimize=True)
        print('saved', igp)
    return arr

# ---- schedule lookup ------------------------------------------------------------------------
SCHEDULE = os.path.join(HERE, 'workshops.json')

def session_kwargs(iso_date):
    """Everything build() needs for one scheduled session in workshops.json."""
    import json
    d = json.load(open(SCHEDULE))
    sess = next((x for x in d['sessions'] if x['date'] == iso_date), None)
    if not sess: raise SystemExit(f'{iso_date} not in {SCHEDULE}')
    ser = d['series'][sess['series']]
    top = d['topics'].get(sess.get('topic') or '', {})
    kw = dict(date=sess['flyer_date'], time=sess['flyer_time'], topic=top.get('name'),
              takehome=top.get('takehome'))
    kw.update(PRESETS[ser['preset']])
    out = f"flyer-{iso_date}-{sess['series']}.png"
    return out, kw

def selftest():
    """Font fit, schedule data, logo files, and a test build of every scheduled session."""
    import json, datetime
    ok = True
    src = np.array(Image.open(TEMPLATE).convert('RGB'))
    # 1) font calibration: re-type the template's own date/time in place, compare ink masks
    arr = src.copy(); erase(arr, DT_BOX, 'ink', 2)
    draw(arr, 'FRI, SEPT 25', POS['date'], min_gap_em=MIN_GAP['date'], **STY['date'])
    draw(arr, '2:30 PM', POS['time'], min_gap_em=MIN_GAP['date'], **STY['date'])
    y0, y1, x0, x1 = DT_BOX
    m1 = src[y0:y1, x0:x1].astype(int).sum(2) < 400; m2 = arr[y0:y1, x0:x1].astype(int).sum(2) < 400
    iou = (m1 & m2).sum() / max((m1 | m2).sum(), 1)
    print(f'selftest font fit (date/time ink overlap): IoU {iou:.3f}'); ok &= iou > 0.85
    # 2) data + assets
    d = json.load(open(SCHEDULE))
    for p in XRAY_LOGOS.values():
        if not os.path.exists(p): print('  missing logo', p); ok = False
    for x in d['sessions']:
        dt = datetime.date.fromisoformat(x['date'])
        want = dt.strftime('%a, %b ').upper() + str(dt.day)
        if x['flyer_date'] != want: print(f"  {x['date']}: flyer_date {x['flyer_date']!r} != {want!r}"); ok = False
        if x['series'] not in d['series'] or x.get('topic') not in d['topics']:
            print(f"  {x['date']}: unknown series/topic"); ok = False
    # 3) build every session (asserts integrity, arrow clearance, line widths)
    os.makedirs(os.path.join(HERE, 'scratch', 'selftest'), exist_ok=True)
    for x in d['sessions']:
        out, kw = session_kwargs(x['date'])
        build(os.path.join(HERE, 'scratch', 'selftest', out), ig=False, **kw)
    print('selftest', 'PASSED' if ok else 'FAILED'); return ok

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--session', help='ISO date in workshops.json (e.g. 2026-10-09): fills date, time, '
                    'venue preset, topic and take-home; other flags still override')
    ap.add_argument('--date'); ap.add_argument('--time'); ap.add_argument('--out')
    ap.add_argument('--preset', choices=PRESETS)
    ap.add_argument('--venue', help='venue heading (replaces "Kiva Cowork")')
    ap.add_argument('--venue-line', action='append', help='venue sub-line (repeat, max 2)')
    ap.add_argument('--logo', choices=['kiva', 'xray', 'xray-badge', 'none'], help='icon/logo inline left of the heading')
    ap.add_argument('--topic', help='topic line under the time, e.g. "The Loop Audit"')
    ap.add_argument('--fade-time', action='store_true')
    ap.add_argument('--tagline', help='right-panel tagline (default: TAGLINE in this file)')
    ap.add_argument('--agenda', action='append', help='agenda line (repeat, max 3; default: AGENDA)')
    ap.add_argument('--takehome', help='take-home line under the agenda, e.g. "Your Loop Audit worksheet"')
    ap.add_argument('--takehome-label', help='header above it (default TAKE-HOME)')
    ap.add_argument('--no-ig', action='store_true')
    ap.add_argument('--batch', action='store_true', help='rebuild the Oct 9 XRAY and Oct 30 Kiva flyers from workshops.json')
    ap.add_argument('--selftest', action='store_true', help='font fit, schedule data and test builds')
    a = ap.parse_args()
    if a.selftest: sys.exit(0 if selftest() else 1)
    if a.batch:
        for iso in ('2026-10-09', '2026-10-30'):
            out, kw = session_kwargs(iso); build(out, **kw)
        sys.exit()
    out, kw = (session_kwargs(a.session) if a.session else (None, {}))
    if a.preset: kw.update(PRESETS[a.preset])
    for k, v in dict(date=a.date, time=a.time, venue=a.venue, lines=a.venue_line, topic=a.topic,
                     takehome=a.takehome, takehome_label=a.takehome_label, tagline=a.tagline,
                     agenda=a.agenda).items():
        if v: kw[k] = v
    if a.logo: kw['logo'] = None if a.logo == 'none' else a.logo
    kw.setdefault('logo', 'kiva' if not kw.get('venue') else None)
    out = a.out or out
    if not (kw.get('date') and kw.get('time') and out): ap.error('need --session, or --date, --time and --out')
    build(out, fade_time=a.fade_time, ig=not a.no_ig, **kw)
