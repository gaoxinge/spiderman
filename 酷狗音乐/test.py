# -*- coding: utf-8 -*-
"""
酷狗音乐
   周杰伦 东风破：http://www.kugou.com/song/74l88f.html
"""
import re
import requests

# get hash
response = requests.get("http://www.kugou.com/song/74l88f.html")
pattern = re.compile(r'"hash":"(.*?)"')
match = pattern.search(response.text)
hash = match.group(1)

# get music url
params = {
   "r": "play/getdata",
   "hash": hash
}
response = requests.get("http://www.kugou.com/yy/index.php", params=params)
result = response.json()
music_url = result["data"]["play_url"]

# get music
response = requests.get(music_url)
with open('dongfengpo.mp3', 'wb') as f:
    f.write(response.content)