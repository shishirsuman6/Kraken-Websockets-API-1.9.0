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

def message_time_baseline(t):
    now= datetime.now()
    now_minus_threshold= now + timedelta(0,t)
    return now_minus_threshold.strftime('%Y-%m-%d %H:%M:%S')

def send_subscribe_book(ws, pair,depth):
    msg_string='{"event": "subscribe", "pair": ["' + str(pair) + '"],"subscription": {"depth": ' + str(depth) + ',"name": "book"}}'
    ws.send(msg_string)

def pytest_html_report_title(report):
    report.title = "Kraken Websockets API 1.9.0 - Test Results"