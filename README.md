# Songs-Index
An index generator for songs that I have on my Music channel on Telegram. The list of songs is parsed and the index is updated automatically using python, by running a single file (`update`).

## Steps to make it work for your own playlist:
1. Run the following to install all the requirements.
```python
pip install -r requirements.txt
```
2. Change the [`songs_path`](update-index.py#L41) and [`index_path`.](update-index.py#L42) (The location where to save the generated index. The file need not exist.)
3. Change the [`format`](update-index.py#L43) to whatever the format your songs are in.
4. Run `update_index.py` to get an index generated for you!

Done!
