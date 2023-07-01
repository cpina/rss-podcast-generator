#!/bin/bash

URL="$1"
DESTINATION_DIR="data/"
yt-dlp --no-mtime --path "$DESTINATION_DIR" --extract-audio --audio-format mp3 "$URL"

