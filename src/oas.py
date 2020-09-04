import os
import re
import shutil
import logging
import string

import colorama
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

colorama.init()

# Match things like: "123 Artist - Song"
# But unfortunately, some are "song - artist", there's no way to tell them apart
song_pattern = r"(?<id>\d+ )?(?<artist>[\w '!+&,]+)(-)?(?<title>[\w ().]+)?"
# I want to be able to test the pattern as I change it
# But RegExr doesn't allow the Python-style group names
song_pattern = song_pattern.replace("?<", "?P<")

between_parenthesis = '\(.*?\)'

logging.getLogger().setLevel(logging.DEBUG)


# noinspection PyShadowingBuiltins
def scrape_songs(src, dest):
    # Loop all song directories in src
    for dir in os.listdir(src):
        match = re.search(song_pattern, dir)
        # id = match.group('id')
        artist = match.group('artist')
        title = match.group('title')

        # Points out anything that didn't match
        if artist is None or title is None:
            warn(f"{dir} was dropped as the artist or song name couldn't be found")
            continue
        else:
            # Remove any text in parenthesis
            if '(' in artist or ')' in artist:
                artist = re.sub(between_parenthesis, '', artist)
            if '(' in title or ')' in title:
                title = re.sub(between_parenthesis, '', title)

            artist = artist.strip()
            title = title.strip()

        # Loops all the files that might be an MP3
        for file in os.listdir(f"{src}\\{dir}"):
            # Checks if it's an MP3
            if file.endswith(".mp3"):
                # Strip the beginning digits of the name
                name = dir.lstrip(string.digits).strip()

                # Strip anything in parenthesis
                if '(' in name or ')' in name:
                    name = re.sub(between_parenthesis, '', name).strip()

                # Copy and rename the file
                shutil.copyfile(f"{src}\\{dir}\\{file}", f"{dest}\\{name}.mp3")

                # Open the MP3
                mp3 = MP3(f"{dest}\\{name}.mp3", ID3=EasyID3)
                # Clear the metadata
                mp3.clear()
                # Add the title and artist
                mp3['title'] = title
                mp3['artist'] = artist
                # Save the changes
                mp3.save()

                debug(f"Processed {name}")
            else:
                warn(f"Ignored {file}")


def debug(text):
    logging.debug(f"{colorama.Fore.CYAN}{text}{colorama.Style.RESET_ALL}")


def warn(text):
    logging.warning(f"{colorama.Fore.RED}{text}{colorama.Style.RESET_ALL}")
