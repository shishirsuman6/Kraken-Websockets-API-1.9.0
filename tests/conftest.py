#--------------------------------------------------------------------
#Imports
#--------------------------------------------------------------------
from numpy import array
import pytest
import websocket
import json
from datetime import datetime, timedelta
from helper_function import *

@pytest.fixture
# def ws(scope="session"):
def ws():
    # Generator setup
    SOCKET = 'wss://ws.kraken.com/'
    # Launch the connection to the server.
    ws_obj = websocket.create_connection(SOCKET)
    yield ws_obj, result(ws_obj)
    # Generator Tear-down
    ws_obj.close()

