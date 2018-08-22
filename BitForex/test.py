# -*- coding: utf-8 -*-
"""
https://cn.bitforex.com/trade/spotTrading
"""
import websocket
import json

url = 'wss://wscn.bitforex.com/mkapi/coinGroup1/ws'
data = [{"type": "subHq", "event": "depth10", "param": {"businessType": "coin-usdt-btc", "dType": 0, "size": 100}}]
ws = websocket.create_connection(url, timeout=10)
ws.send(json.dumps(data))
for i in range(5):
    content = ws.recv()
    print content
ws.close()