# Automate Your Business flyers

CURRENT (correct) template: src/template-correct.png (2320x2720)
  = attachment "automate-your-business-workshop.png" on the Sep 25, 2026 email
    "Updated Flyer for Automate Your Business".
  The "event flyer" link in that email goes to Canva: her Canva account (link kept private)
    (editable source; needs Rachael's Canva login)
  src/email-attachment-automate-your-business-workshop.png: the same file as downloaded

Runbook:   PROCESS.md (how to create, check and update these flyers; start here)
Generator: make_flyers_v2.py (see its docstring for usage)
           .venv/bin/python make_flyers_v2.py --session 2026-11-13   (cairosvg lives in that venv)
Schedule:  workshops.json (both series, topics, take-homes)
Logos:     src/logos/ (official XRAY SVGs from Rachael; flyer uses xray-logo-b, the wordmark)
Captions:  captions.md (drafts, not posted)
Outputs:   flyer-2026-10-30-kiva.png, flyer-2026-10-09-xray.png (2320x2720)
           previews/ig-flyer-*.png (1080x1350 Instagram 4:5)
Superseded (wrong template): superseded/, make_flyers.py, src/flyer-rebuilt-*, src/poster-*
