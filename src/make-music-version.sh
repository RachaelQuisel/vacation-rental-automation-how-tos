#!/usr/bin/env bash
# Makes the 20 s music version of a wide 10 s loop.
# The loop plays twice, and a 20 s excerpt of a music track is added
# with short fades and two-pass loudness normalization (-16 LUFS).
#
# Usage: ./make-music-version.sh <loop-1920x1080.mp4> <track.mp3> <excerpt-start-seconds> <output.mp4>
# Example (cleaner video): ./make-music-version.sh out/loop-1920x1080.mp4 le-croissant.mp3 76.95 out/schedule-cleaners-by-text.mp4
#
# The track is not in this repo. Download it from its source page and keep
# the CC BY 4.0 credit next to the video wherever you publish it.
set -euo pipefail
IN=$1; A=$2; S=$3; OUTF=$4
AF="atrim=start=$S:duration=20,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.3,afade=t=out:st=18.5:d=1.5"

# Pass 1: measure loudness of the excerpt.
J=$(ffmpeg -hide_banner -nostats -i "$A" -af "$AF,loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p')
g(){ echo "$J" | python3 -c "import json,sys;print(json.load(sys.stdin)['$1'])"; }
MI=$(g input_i); MTP=$(g input_tp); MLRA=$(g input_lra); MT=$(g input_thresh); OFF=$(g target_offset)
echo "pass1: I=$MI TP=$MTP LRA=$MLRA thresh=$MT offset=$OFF"

# Pass 2: apply the measured values, copy the video stream, play it twice.
ffmpeg -y -loglevel error -stream_loop 1 -i "$IN" -i "$A" -filter_complex \
 "[1:a]$AF,loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=$MI:measured_TP=$MTP:measured_LRA=$MLRA:measured_thresh=$MT:offset=$OFF:linear=true,aresample=48000[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -ac 2 -t 20 -movflags +faststart "$OUTF"

# Check the result.
ffmpeg -hide_banner -nostats -i "$OUTF" -af loudnorm=I=-16:print_format=summary -f null - 2>&1 | grep -E "Input Integrated|Input True Peak"
ffprobe -v error -show_entries stream=codec_name,width,height,pix_fmt,sample_rate,channels -show_entries format=duration,size -of compact=p=0 "$OUTF"
