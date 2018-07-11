# -*- coding: utf-8 -*-
"""
百度音乐：
  东风破：http://music.taihe.com/song/260166
  只要平凡：http://music.taihe.com/song/598740690
"""
import requests

# song info
data = {"songIds": 598740690}
response = requests.post("http://play.taihe.com/data/music/songinfo", data=data)
result1 = response.json()
print result1

data = {"songIds": 260166}
response = requests.post("http://play.taihe.com/data/music/songinfo", data=data)
result2 = response.json()
print result2

# song link
data = {
    "songIds": "260166,598740690",
    "hq": "0",
    "type": "m4a,mp3",
    "rate": "",
    "pt": "0",
    "flag": "-1",
    "s2p": "-1",
    "prerate": "-1",
    "bwt": "-1",
    "dur": "-1",
    "bat": "-1",
    "bp": "-1",
    "pos": "-1",
    "auto": "-1"
}
response = requests.post("http://play.taihe.com/data/music/songlink", data=data)
result = response.json()
song_list = result["data"]["songList"]
song_link = [song["songLink"] for song in song_list]
print song_link

# download
i = 0
for song in song_link:
    i += 1
    response = requests.get(song)
    with open("{i}.mp3".format(i=i), "wb") as f:
        f.write(response.content)
