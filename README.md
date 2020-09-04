# oas
A script to scrape songs from your Osu folder.

### Pitch
Are you ever so lazy that you don't want to individually download and copy music to your phone? Are you an Osu player?

Then you probably have a big library of songs. This script will go through and organise these songs into a folder for you.

### Usage
From the directory containing this folder:
```batch
python oas C:\osu C:\Music
```
You can check the version with:
```batch
python oas -v
```
You can check the details with:
```batch
python oas -h
```

### Details
- Songs are renamed to the folder they're contained in, without the ID at the start
- The copied songs will have their metadata wiped, and a new title and artist added
- Any text in parenthesis are removed from the; filename, title and artist
