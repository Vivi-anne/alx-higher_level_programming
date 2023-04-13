#!/usr/bin/python3
"""modules defines json file-reading function"""
import json


def load_from_json_file(filename):
    """python object created from json file"""
    with open(filename) as f:
        return json.load(f)
