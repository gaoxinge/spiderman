# -*- coding: utf-8 -*-
"""
https://www.okcoin.com/market
"""
import websocket
import zlib

url = 'wss://real.okcoin.com:10440/websocket'
ws = websocket.create_connection(url, timeout=10)
ws.send("""{event:'addChannel',parameters:{"base":"btc","binary":"1","product":"spot","quote":"usd","type":"depth"}}""")
for i in range(5):
    content_compress = ws.recv()
    content = zlib.decompress(content_compress, -zlib.MAX_WBITS)
    print content
ws.close()
