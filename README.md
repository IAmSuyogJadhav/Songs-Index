# Songs-Index
An index generator for songs that I have on my Music channel on Telegram. The list of songs is parsed and the index is updated automatically using python, by running a single file (`update`).

## Steps to make it work for your own playlist:
1. Make sure your filenames occur in a fixed format containing both the song's title as well as the singers' names.
2. Change the regex pattern on line [#10](update-index.py#L10) of [update-index.py](update-index.py) to match the filename pattern of your songs.
3. Change the [`songs_path`](update-index.py#L41) and [`index_path`.](update-index.py#L42) (The location where to save the generated index. The file need not exist.)
4. Change the [`format`](update-index.py#L43) to whatever the format your songs are in.

Done!
