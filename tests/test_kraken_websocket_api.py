"""
The purpose of this test is to show how to use the pytest framework for Kraken Websockets API 1.9.0
"""
#--------------------------------------------------------------------
#Imports
#--------------------------------------------------------------------
from numpy import array
import pytest
import websocket
import json
from datetime import datetime, timedelta
from helper_function import *

#--------------------------------------------------------------------
# Tests
#--------------------------------------------------------------------
@pytest.mark.websocket_connection
def test_websocket_connection_event(ws):
    assert ws[1]["event"]=="systemStatus"

@pytest.mark.websocket_connection
def test_websocket_connection_status(ws):
    assert ws[1]["status"]=="online"

@pytest.mark.websocket_connection
def test_websocket_connection_version(ws):
    assert ws[1]["version"]=="1.9.0"

@pytest.mark.websocket_connection
def test_websocket_connection_schema(ws):
    assert 'connectionID' in ws[1]    

@pytest.mark.ping
def test_ping(ws):
    ws[0].send(json.dumps({"event": "ping","reqid": 1}))
    assert result(ws[0]) == json.loads('{"event":"pong","reqid":1}')