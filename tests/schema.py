"""
The purpose of this file is to store the message schemas to use the pytest framework for Kraken Websockets API 1.9.0
"""
#--------------------------------------------------------------------
#Imports
#--------------------------------------------------------------------
import json
from jsonschema import validate


#--------------------------------------------------------------------
# Schemas
#--------------------------------------------------------------------

schema_pong = {"type" : "object", 
                "properties" : { 
                    "event" : {"type" : "string"}, 
                    "reqid" : {"type" : "integer"} }}

schema_pong_error_event = {"type" : "object", 
                            "properties" : { 
                                "errorMessage" : {"type" : "string"}, 
                                "event" : {"type" : "string"},
                                "reqid" : {"type" : "integer"},
                                "status" : {"type" : "string"} }}

schema_pong_error_reqid = {"type" : "object", 
                            "properties" : { 
                                "errorMessage" : {"type" : "string"}, 
                                "event" : {"type" : "string"} }}

schema_systemStatus = {"type" : "object", 
                        "properties" : { 
                            "connectionID" : {"type" : "integer"}, 
                            "event" : {"type" : "string"},
                            "status" : {"type" : "string"},
                            "version" : {"type" : "string"} }}

schema_subscriptionStatus = {"type" : "object", 
                                "properties" : { 
                                    "channelName" : {"type" : "string"}, 
                                    "event" : {"type" : "string"},
                                    "reqid" : {"type" : "integer"},
                                    "pair" : {"type" : "string"},
                                    "status" : {"type" : "string"},
                                    "subscription" : { "type" : "object",
                                                        "properties" : { 
                                                            "depth" : {"type" : "integer"}, 
                                                            "interval" : {"type" : "integer"},
                                                            "maxratecount" : {"type" : "integer"},
                                                            "name" : {"type" : "string"},
                                                            "token" : {"type" : "string"}}},
                                    "OneOf" : { "type" : "object",
                                                        "properties" : { 
                                                            "errorMessage" : {"type" : "string"}, 
                                                            "channelID" : {"type" : "integer"}}} }}              


schema_book_publication_snapshot = {"type" : "array", 
                                        "properties" : { 
                                            "channelID" : {"type" : "integer"}, 
                                            "channelName" : {"type" : "string"},
                                            "pair" : {"type" : "string"},
                                            "": {"type" : "object",
                                                        "properties" : { 
                                                            "as" : {"type" : "array",  
                                                                        "items":{"price" : {"type" : "decimal"},
                                                                                "volume" : {"type" : "decimal"},
                                                                                "timestamp" : {"type" : "decimal"} } },
                                                            "bs" : {"type" : "array",  
                                                                        "items":{"price" : {"type" : "decimal"},
                                                                                "volume" : {"type" : "decimal"},
                                                                                "timestamp" : {"type" : "decimal"} } }
                                                                        }} }}

schema_book_publication_update = {"type" : "array", 
                                        "properties" : { 
                                            "channelID" : {"type" : "integer"}, 
                                            "channelName" : {"type" : "string"},
                                            "pair" : {"type" : "string"},
                                            "AnyOf": { "anyOf" : [{
                                                            "": {"type" : "object",
                                                                    "properties" : { 
                                                                        "a" : {"type" : "array",  
                                                                                    "items":{"price" : {"type" : "decimal"},
                                                                                            "volume" : {"type" : "decimal"},
                                                                                            "timestamp" : {"type" : "decimal"},
                                                                                            "updateType" : {"type" : "string"} } },
                                                                        "c" : {"type" : "string"}}},
                                                            "": {"type" : "object",
                                                                    "properties" : { 
                                                                        "b" : {"type" : "array",  
                                                                                    "items":{"price" : {"type" : "decimal"},
                                                                                            "volume" : {"type" : "decimal"},
                                                                                            "timestamp" : {"type" : "decimal"},
                                                                                            "updateType" : {"type" : "string"} } },
                                                                        "c" : {"type" : "string"}}}}]}}}


schema_spread_publication = {"type" : "array", 
                                "properties" : { 
                                    "channelID" : {"type" : "integer"}, 
                                    "channelName" : {"type" : "string"},
                                    "pair" : {"type" : "string"},
                                    "properties":{"type" : "array",  
                                                    "items":{
                                                        "bid" : {"type" : "decimal"},
                                                        "ask" : {"type" : "decimal"},
                                                        "timestamp" : {"type" : "decimal"},
                                                        "bidVolume" : {"type" : "decimal"},
                                                        "askVolume" : {"type" : "decimal"} } }}}

schema_trade_publication = {"type" : "array", 
                        "properties" : { 
                            "channelID" : {"type" : "integer"}, 
                            "channelName" : {"type" : "string"},
                            "pair" : {"type" : "string"},
                            "":{"type" : "array",  
                                "items":{
                                    "":{"type" : "array",  
                                        "items":{
                                                "price" : {"type" : "decimal"},
                                                "volume" : {"type" : "decimal"},
                                                "time" : {"type" : "decimal"},
                                                "side" : {"type" : "string"},
                                                "orderType" : {"type" : "string"},
                                                "misc" : {"type" : "string"}} }}}}}

schema_ohlc_publication = {"type" : "array", 
                                "properties" : { 
                                    "channelID" : {"type" : "integer"}, 
                                    "channelName" : {"type" : "string"},
                                    "pair" : {"type" : "string"},
                                    "properties":{"type" : "array",  
                                                    "items":{
                                                        "time" : {"type" : "decimal"},
                                                        "etime" : {"type" : "decimal"},
                                                        "open" : {"type" : "decimal"},
                                                        "high" : {"type" : "decimal"},
                                                        "low" : {"type" : "decimal"},
                                                        "close" : {"type" : "decimal"},
                                                        "vwap" : {"type" : "decimal"},
                                                        "volume" : {"type" : "decimal"},
                                                        "count" : {"type" : "integer"} } }}}