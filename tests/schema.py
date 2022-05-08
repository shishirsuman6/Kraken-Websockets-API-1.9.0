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