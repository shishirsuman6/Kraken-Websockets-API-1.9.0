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
from jsonschema import validate
from datetime import datetime, timedelta
from helper_function import *
from schema import *

#--------------------------------------------------------------------
# Tests
#--------------------------------------------------------------------
@pytest.mark.book_subscription
def test_subscribe_book_subscriptionStatus_response_channelID(ws):
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    assert type(subscriptionStatus_response['channelID']) == int

@pytest.mark.book_subscription
def test_subscribe_book_subscriptionStatus_response_channelName(ws):
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    assert subscriptionStatus_response["channelName"]=="book-10"  

@pytest.mark.book_subscription
def test_subscribe_book_subscriptionStatus_response_event(ws):
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    assert subscriptionStatus_response["event"]=="subscriptionStatus"  

@pytest.mark.book_subscription
def test_subscribe_book_subscriptionStatus_response_pair(ws):
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    assert subscriptionStatus_response["pair"]=="XBT/USD"

@pytest.mark.book_subscription
def test_subscribe_book_subscriptionStatus_response_status(ws):
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    assert subscriptionStatus_response["status"]=="subscribed"

@pytest.mark.book_subscription
def test_subscribe_book_subscriptionStatus_response_subscription_depth(ws):
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    assert subscriptionStatus_response["subscription"]["depth"]==10

@pytest.mark.book_subscription
def test_subscribe_book_subscriptionStatus_response_subscription_name(ws):
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    assert subscriptionStatus_response["subscription"]["name"]=="book" 


@pytest.mark.book_publication
def test_subscribe_book_publication_schema_length(ws):
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    next_message= result(ws[0])    
    if 'event' in next_message:
        book_publication= result(ws[0])
    else:
        book_publication=next_message

    assert len(book_publication) == 4


@pytest.mark.book_publication
def test_subscribe_book_publication_schema_channelID(ws):
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    channelID= subscriptionStatus_response['channelID']
    next_message= result(ws[0])    
    if 'event' in next_message:
        book_publication= result(ws[0])
    else:
        book_publication=next_message

    assert book_publication[0] == channelID


@pytest.mark.book_publication
def test_subscribe_book_publication_schema_depth(ws):
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    next_message= result(ws[0])    
    if 'event' in next_message:
        book_publication= result(ws[0])
    else:
        book_publication=next_message

    assert book_publication[2] == "book-10"


@pytest.mark.book_publication
def test_subscribe_book_publication_schema_pair(ws):
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    next_message= result(ws[0])    
    if 'event' in next_message:
        book_publication= result(ws[0])
    else:
        book_publication=next_message

    assert book_publication[3] == "XBT/USD"


@pytest.mark.book_publication
def test_subscribe_book_publication_schema_ask_length(ws):
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    next_message= result(ws[0])    
    if 'event' in next_message:
        book_publication= result(ws[0])
    else:
        book_publication=next_message
    assert len(book_publication[1]["as"]) == 10


@pytest.mark.book_publication
def test_subscribe_book_publication_schema_bid_length(ws):
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    next_message= result(ws[0])    
    if 'event' in next_message:
        book_publication= result(ws[0])
    else:
        book_publication=next_message
    assert len(book_publication[1]["bs"]) == 10

@pytest.mark.book_publication
def test_subscribe_book_publication_schema_ask_element_length(ws):
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    next_message= result(ws[0])    
    if 'event' in next_message:
        book_publication= result(ws[0])
    else:
        book_publication=next_message
    assert len(book_publication[1]["as"][0]) == 3


@pytest.mark.book_publication
def test_subscribe_book_publication_schema_bid_element_length(ws):
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    next_message= result(ws[0])    
    if 'event' in next_message:
        book_publication= result(ws[0])
    else:
        book_publication=next_message
    assert len(book_publication[1]["bs"][0]) == 3


   
@pytest.mark.book_publication
def test_subscribe_book_publication_ask_timestamp(ws):
    t=-2
    timestamp_threshold= message_time_baseline(t)
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    next_message= result(ws[0])    
    if 'event' in next_message:
        book_publication= result(ws[0])
    else:
        book_publication=next_message   
   
    max_ask_price_timestamp=float(book_publication[1]["as"][0][2])
    for i in range(1,10):
        if max_ask_price_timestamp< float(book_publication[1]["as"][i][2]):
            max_ask_price_timestamp=float(book_publication[1]["as"][i][2])
    max_ask_price_timestamp=datetime.fromtimestamp(max_ask_price_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    assert max_ask_price_timestamp >= timestamp_threshold, "No Price change in the last 5 seconds"

@pytest.mark.book_publication
def test_subscribe_book_publication_bid_timestamp(ws):
    t=-2
    timestamp_threshold= message_time_baseline(t)
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    next_message= result(ws[0])    
    if 'event' in next_message:
        book_publication= result(ws[0])
    else:
        book_publication=next_message   
    
    max_bid_price_timestamp=float(book_publication[1]["bs"][0][2])
    for i in range(1,10):
        if max_bid_price_timestamp< float(book_publication[1]["bs"][i][2]):
            max_bid_price_timestamp=float(book_publication[1]["bs"][i][2])
    max_bid_price_timestamp=datetime.fromtimestamp(max_bid_price_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    
    assert max_bid_price_timestamp >= timestamp_threshold, "No Price change in the last 5 seconds"


@pytest.mark.book_publication
def test_subscribe_book_heartbeat(ws):
    t=-2
    timestamp_threshold= message_time_baseline(t)
    pair='BTC/USD'
    depth=10
    send_subscribe_book(ws[0], pair,depth)
    subscriptionStatus_response= result(ws[0])
    next_message= result(ws[0])    
    if 'event' in next_message:
        assert next_message["event"] == "heartbeat"