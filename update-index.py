import os
import math
import re
from datetime import datetime
import pandas as pd


def parse_songs(_songs):
    pattern = re.compile(r'(.+) - (.+) \[.+\.m4a')
    parsed = []
    bad = []
    step = 25 / len(_songs)

    for i, song in enumerate(_songs):
        stamp = datetime.fromtimestamp(os.path.getmtime(telegram_path + song))
        date = '-'.join(list(map(str, [stamp.day, stamp.month, stamp.year])))

        try:
            name, authors = re.findall(pattern, song)[0]
            authors = ', '.join(authors.split('_ '))
            parsed.append([name, authors, date])
        except IndexError:  # Happens if the name is not correctly formatted
            bad.append(song)
            parsed.append([re.findall(r'(.+)\.m4a', song)[0], 'Unknown', date])

        print('\r' + f'Progress: '
              f"[{'=' * int((i+1) * step) + ' ' * (24 - int((i+1) * step))}]"
              f"({math.ceil((i+1) * 100 / len(_songs))} %)",
              end='')

    print('\n')
    if len(bad):
        print('WARNING: Following bad filenames were found.', *bad, sep="\n\t")
    return pd.DataFrame(parsed,
                        columns=["Song Title", "Authors", "Date Modified"],
                        )


# Path to the Telegram Downloads folder and the index
telegram_path = r'/home/anon/Downloads/Telegram Desktop/'
index_path = r'/home/anon/Interest/Projects/Songs-Index/index.xlsx'

print("#######################################################")
print("\nLoading the list of songs....", end='')
songs = [filename for filename in os.listdir(telegram_path)
         if filename.endswith('.m4a')]
# Sort by date modified
songs = sorted(songs,
               key=lambda x: os.path.getmtime(telegram_path + x),
               reverse=False)
print('Done')
print(f"\nTotal no. of songs in the playlist: {len(songs)}")
print("Parsing songs....")

parsed = parse_songs(songs)

print('Done.')
print("Saving the Index file....", end='')

try:
    parsed.to_excel(index_path, index=True, sheet_name='Songs')  #, sep='\t')
    print('Done')

except Exception as e:
    print("Error.\nCouldn't save file. Try again.\n"
          f"Current saving path:\n\t {index_path}"
          f"\nError Description:\n\t{e}")

print("\n#######################################################")
