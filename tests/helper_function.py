"""
The purpose of this test file is to store helper functions for the pytest framework for Kraken Websockets API 1.9.0
"""
#--------------------------------------------------------------------
#Imports
#--------------------------------------------------------------------
from numpy import array
import pytest
import websocket
import json
from datetime import datetime, timedelta

# #--------------------------------------------------------------------
# # functions
# #--------------------------------------------------------------------

def result(ws):
    return json.loads(ws.recv())

def book_message_time_baseline():
    now= datetime.now()
    now_minus_threshold= now + timedelta(0,-2)
    return now_minus_threshold.strftime('%Y-%m-%d %H:%M:%S')

def send_subscribe_book(ws, pair,depth):
    msg_string='{"event": "subscribe", "pair": ["BTC/USD"],"subscription": {"depth": 10,"name": "book"}}'
    ws.send(msg_string)