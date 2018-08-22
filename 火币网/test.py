# -*- coding: utf-8 -*-
"""
https://www.hbg.com/zh-cn/
"""
import websocket
import json
import zlib

url = 'wss://www.hbg.com/-/s/pro/ws'
data = {"sub":"market.overview"}
ws = websocket.create_connection(url, timeout=10)
ws.send(json.dumps(data))
for i in range(5):
    content_compress = ws.recv()
    content = zlib.decompress(content_compress, 16+zlib.MAX_WBITS)
    print content
ws.close()