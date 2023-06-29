#!/usr/bin/env python3

import argparse
import mimetypes
import os
import time
from datetime import datetime

import feedgenerator
from pathlib import Path



def create_rss(base_url: str, data: Path):
    fg = feedgenerator.Rss201rev2Feed("For Les with love", base_url, "A Happy Podcast for Les")

    # Iterate over directory
    for audio_file in data.iterdir():
        if audio_file.name.endswith('.mp3') or audio_file.name.endswith('.ogg'):
            title = audio_file.stem
            pubdate = audio_file.stat().st_mtime
            pubdate = datetime.fromtimestamp(pubdate)
            link = f"{base_url}/{audio_file.name}"
            mime_type = mimetypes.guess_type(audio_file.name)[0]
            enclosure = feedgenerator.Enclosure(url=link, length=str(audio_file.stat().st_size), mime_type=mime_type)

            fg.add_item(title=title, pubdate=pubdate, link=base_url, description="", enclosure=enclosure)

    # Write the RSS file
    rss_file = os.path.join(data, 'podcast.rss')

    with open(rss_file, "wb") as file:
        fg.write(file, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create an RSS file from audio files in a directory.')
    parser.add_argument("base_url", help='Base URL for the links')
    parser.add_argument("dir", help='The directory containing .mp3 or .ogg files', type=Path)

    args = parser.parse_args()
    create_rss(args.base_url, args.dir)
