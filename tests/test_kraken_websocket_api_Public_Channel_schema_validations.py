"""
The purpose of this test is to show how to use the pytest framework for Kraken Websockets API 1.9.0
"""
#--------------------------------------------------------------------
#Imports
#--------------------------------------------------------------------
from ast import Break
from numpy import array
import pytest
import websocket
import json
from jsonschema import validate
from datetime import datetime, timedelta
from helper_function import *
from schema import *

#--------------------------------------------------------------------
# Tests
#--------------------------------------------------------------------

@pytest.mark.spread_publication
def test_subscribe_spread_publication_schema_validation(ws):
    pair='BTC/USD'
    send_subscribe_spread(ws[0], pair)
    subscriptionStatus_response= result(ws[0])
    next_message= result(ws[0])    
    if 'event' in next_message:
        spread_publication= result(ws[0])
    else:
        spread_publication=next_message
    validate(spread_publication, schema_spread_publication)

@pytest.mark.trade_publication
def test_subscribe_trade_publication_schema_validation(ws):
    pair='BTC/USD'
    send_subscribe_trade(ws[0], pair)
    subscriptionStatus_response= result(ws[0])
    next_message= result(ws[0])
    flag=False

    while True:           
        if 'event' not in next_message:
            flag=True
        if flag:
            break            
        next_message= result(ws[0]) 
    
    trade_publication=next_message 
    validate(trade_publication, schema_trade_publication)

# @pytest.mark.ohlc_publication
# def test_subscribe_ohlc_publication_schema_validation(ws):
#     pair='XBT/EUR'
#     interval=21600
#     send_subscribe_ohlc(ws[0], pair, interval)
#     #subscriptionStatus_response= result(ws[0])
#     next_message= result(ws[0])
#     flag=False

#     while True:           
#         if ('status' not in next_message) or ('event' not in next_message):
#             flag=True
#         if flag:
#             break            
#         next_message= result(ws[0]) 
    
#     ohlc_publication=next_message 
#     validate(ohlc_publication, schema_trade_publication)
