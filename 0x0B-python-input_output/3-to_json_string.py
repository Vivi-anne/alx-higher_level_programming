#!/usr/bin/python3
"""
modules defines a string to JSON function
"""
import json



def to_json_string(my_obj):
    """returns json representation of a string object"""
    return json.dumps(my_obj)
