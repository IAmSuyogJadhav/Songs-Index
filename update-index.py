import os
import math
import sys
from tinytag import TinyTag as tag
import pandas as pd


def parse_songs(_songs):
    parsed = []
    step = 25 / len(_songs)

    for i, song in enumerate(_songs):
        tags = tag.get(songs_path + song)

        title = tags.title if tags.title else song[:-4]
        year = tags.year if tags.year else 'Unknown'
        artists = tags.artist if tags.artist else 'Unknown'
        album = tags.album if (tags.album is None
                               or tags.album.lower() != 'www.chiasenhac.com'
                               ) else 'Unknown'
        genre = tags.genre if tags.genre else 'Unknown'

        parsed.append([title, album, artists, genre, year])

        print('\r' + f'Progress: '
              f"[{'=' * int((i+1) * step) + ' ' * (24 - int((i+1) * step))}]"
              f"({math.ceil((i+1) * 100 / len(_songs))} %)",
              end='')

    print('\n')
    return pd.DataFrame(parsed,
                        columns=["Song Title", "Album",
                                 "Artists", "Genre", "Year"],
                        index=range(1, len(parsed)+1)
                        )


# Path to the songs folder and the index file
songs_path = r'/home/anon/Downloads/Telegram Desktop/'
index_path = r'/home/anon/Interest/Projects/Songs-Index/index.xlsx'
format = '.m4a'

print("#######################################################")
print("\nLoading the list of songs....", end='')
songs = [filename for filename in os.listdir(songs_path)
         if filename.endswith(format)]
# Sort by Name
songs = sorted(songs)
print('Done')
print(f"\nTotal no. of songs in the playlist: {len(songs)}")
print("Parsing songs....")

# print(songs)  # DEBUG
parsed = parse_songs(songs)
# print(parsed)  # DEBUG
print('Done.')
print("Saving the Index file....", end='')

writer = pd.ExcelWriter(index_path, engine='xlsxwriter')
try:
    parsed.to_excel(writer, sheet_name='Songs-Index')
    worksheet = writer.sheets['Songs-Index']
    pad = 1  # Additional padding per column

    for idx, col in enumerate(parsed):
        series = parsed[col]
        max_len = max(
            series.astype(str).map(len).max(),
            len(str(series.name))
        ) + pad

        worksheet.set_column(idx, idx, max_len)

    writer.save()
except Exception as e:
    print("\nERROR: Couldn't save file. Something went wrong.\n"
          f"Current saving path:\n\t {index_path}"
          f"\nError Description:\n\t{e}")
    sys.exit(1)

print('Done')

print("\n#######################################################\n")
