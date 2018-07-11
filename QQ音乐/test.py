# -*- coding: utf-8 -*-
import json
import requests
"""
QQ音乐
  七里香：https://y.qq.com/n/yqq/song/002ZKnKQ34rbZu.html
"""


# get music url
songmid = "002ZKnKQ34rbZu"
callback = "MusicJsonCallback6677699909264738"
guid = "4833370435"
uin = "0"
params = {
    "g_tk": "5381",
    "jsonpCallback": callback,
    "loginUin": "0",
    "hostUin": "0",
    "format": "json",
    "inCharset": "utf8",
    "outCharset": "utf-8",
    "notice": "0",
    "platform": "yqq",
    "needNewCode": "0",
    "cid": "205361747",
    "callback": callback,
    "uin": uin,
    "songmid": songmid,
    "filename": "C400{songmid}.m4a".format(songmid=songmid),
    "guid": guid
}
response = requests.get("https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg", params=params)
result = response.text[len(callback)+1:-1]
result = json.loads(result)
result = result["data"]["items"][0]


# get music
file_name = result["filename"]
params = {
    "vkey": result["vkey"],
    "guid": guid,
    "uin": uin,
    "fromtag": 66
}
response = requests.get("http://dl.stream.qqmusic.qq.com/{file_name}".format(file_name=file_name), params=params)
with open('qilixiang.m4a', 'wb') as f:
    f.write(response.content)
