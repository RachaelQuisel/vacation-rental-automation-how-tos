#!/usr/bin/env bash
# Renders the "Schedule your cleaners by text" video (v1.html).
# Makes the wide and square silent loops, the two posters, and QC frames.
# Run from anywhere. Output goes to src/out/ unless OUT is set.
#   ./render-v1.sh
#   OUT=/tmp/v1-out ./render-v1.sh
set -euo pipefail
cd "$(dirname "$0")"
OUT=${OUT:-out}
export DUR=${DUR:-10}
mkdir -p "$OUT/frames-wide" "$OUT/frames-square" "$OUT/qc"
rm -f "$OUT"/frames-wide/*.png "$OUT"/frames-square/*.png

# 1. Capture frames, wide and square at the same time.
node cap.js v1.html "$OUT/frames-wide" 1920 1080 & p1=$!
node cap.js v1.html "$OUT/frames-square" 1080 1080 '?sq' & p2=$!
wait $p1; wait $p2

# 2. Encode silent H.264 loops that every browser can play.
E="-c:v libx264 -pix_fmt yuv420p -preset slow -crf 22 -movflags +faststart -an"
ffmpeg -y -loglevel error -framerate 30 -i "$OUT/frames-wide/f%04d.png" $E "$OUT/loop-1920x1080.mp4"
ffmpeg -y -loglevel error -framerate 30 -i "$OUT/frames-square/f%04d.png" $E "$OUT/loop-1080x1080.mp4"

# 3. Posters: frame 240 (8.0 s) shows the finished calendar, step 3, and the note.
if [ -f "$OUT/frames-wide/f0240.png" ]; then
  cp "$OUT/frames-wide/f0240.png" "$OUT/poster.png"
  cp "$OUT/frames-square/f0240.png" "$OUT/poster-square.png"
fi

# 4. QC frames to look at by eye: every step and the loop reset.
for t in 0.2 1.8 3.5 4.8 6.3 8.0 9.4 9.95; do
  ffmpeg -y -loglevel error -ss $t -i "$OUT/loop-1920x1080.mp4" -frames:v 1 "$OUT/qc/wide-$t.png" || true
  ffmpeg -y -loglevel error -ss $t -i "$OUT/loop-1080x1080.mp4" -frames:v 1 "$OUT/qc/square-$t.png" || true
done

# 5. Format check: expect h264, yuv420p, the right size, and DUR seconds.
for f in "$OUT"/loop-*.mp4; do
  ffprobe -v error -show_entries stream=codec_name,pix_fmt,width,height -show_entries format=duration -of compact=p=0 "$f"
done
ls -la "$OUT"/*.mp4 "$OUT"/*.png 2>/dev/null || true
