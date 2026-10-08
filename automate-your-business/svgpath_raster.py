"""Tiny rasterizer for simple filled SVG logos (M/L/H/V/C/Z path commands, abs+rel, even-odd fill).
Used for the official XRAY logo (src/xray-logo/logo-xray.svg) so no cairo dependency is needed."""
import re, numpy as np
from PIL import Image, ImageDraw

def _tokens(d):
    return re.findall(r'[MmLlHhVvCcZz]|-?\d*\.?\d+(?:e-?\d+)?', d)

def _subpaths(d, steps=24):
    t = _tokens(d); i = 0; cmd = None; x = y = sx = sy = 0.0; cur = []; out = []
    def num():
        nonlocal i; v = float(t[i]); i += 1; return v
    while i < len(t):
        if re.match(r'[A-Za-z]', t[i]): cmd = t[i]; i += 1
        rel = cmd.islower(); C = cmd.upper()
        if C == 'Z':
            if cur: out.append(cur); cur = []
            x, y = sx, sy; continue
        if C == 'M':
            nx, ny = num(), num()
            if rel: nx += x; ny += y
            if cur: out.append(cur)
            x, y = sx, sy = nx, ny; cur = [(x, y)]; cmd = 'l' if rel else 'L'; continue
        if C == 'L':
            nx, ny = num(), num(); x, y = (x + nx, y + ny) if rel else (nx, ny); cur.append((x, y))
        elif C == 'H':
            nx = num(); x = x + nx if rel else nx; cur.append((x, y))
        elif C == 'V':
            ny = num(); y = y + ny if rel else ny; cur.append((x, y))
        elif C == 'C':
            p = [num() for _ in range(6)]
            if rel: p = [p[k] + (x if k % 2 == 0 else y) for k in range(6)]
            x0, y0 = x, y
            for s in range(1, steps + 1):
                u = s / steps; a, b, c, e = (1-u)**3, 3*u*(1-u)**2, 3*u*u*(1-u), u**3
                cur.append((a*x0 + b*p[0] + c*p[2] + e*p[4], a*y0 + b*p[1] + c*p[3] + e*p[5]))
            x, y = p[4], p[5]
    if cur: out.append(cur)
    return out

def render_svg(path, height_px, S=8):
    """Return (alpha float array HxW in 0..1, fill color (r,g,b)) at the given pixel height."""
    svg = open(path).read()
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
    scale = height_px * S / vb[3]
    W, H = int(np.ceil(vb[2] * scale)), int(np.ceil(vb[3] * scale))
    acc = np.zeros((H, W), bool); color = None
    for m in re.finditer(r'<path\b[^>]*>', svg):
        tag = m.group(0)
        d = re.search(r'\sd="([^"]+)"', tag).group(1)
        fm = re.search(r'fill="([^"]+)"', tag); fill = fm.group(1) if fm else None
        if fill and fill.startswith('#'): color = tuple(int(fill[k:k+2], 16) for k in (1, 3, 5))
        mask = np.zeros((H, W), bool)
        for sp in _subpaths(d):                     # even-odd: XOR each subpath
            im = Image.new('1', (W, H), 0)
            ImageDraw.Draw(im).polygon([((px - vb[0]) * scale, (py - vb[1]) * scale) for px, py in sp], fill=1)
            mask ^= np.asarray(im, bool)
        acc |= mask
    im = Image.fromarray((acc * 255).astype(np.uint8)).resize((max(1, W // S), max(1, H // S)), Image.LANCZOS)
    return np.asarray(im, float) / 255.0, color
