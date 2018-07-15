# -*- coding: utf-8 -*-
"""
b站视频字幕：https://www.bilibili.com/video/av24406116
"""
import codecs
import re
import requests

# get cid
response = requests.get("https://www.bilibili.com/video/av24406116")
pattern = re.compile(r'"cid":(.*?),')
match = pattern.search(response.text)
cid = match.group(1)

# get chat
params = {
    "oid": cid
}
response = requests.get("https://api.bilibili.com/x/v1/dm/list.so", params=params)
response.encoding = 'utf-8'
pattern = re.compile(r'<d p=".*?">(.*?)</d>')
matchs = pattern.findall(response.text)
for match in matchs:
    try:
        print match
    except:
        print match.encode("utf-8")
