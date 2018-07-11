# -*- coding: utf-8 -*-
"""
酷我音乐
  周杰伦东风破：http://bd.kuwo.cn/yinyue/6872015
  对应music：http://antiserver.kuwo.cn/anti.s?format=aac|mp3&rid=MUSIC_6872015&type=convert_url&response=res
"""
import requests

response = requests.get('http://antiserver.kuwo.cn/anti.s?format=aac|mp3&rid=MUSIC_6872015&type=convert_url&response=res')
with open('dongfengpo.aac', 'wb') as f:
    f.write(response.content)