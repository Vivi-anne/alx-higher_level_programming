#!/usr/bin/python3
"""defines python class to json function"""


def class_to_json(obj):
    """returns dictionary representation of data structure"""
    return obj.__dict__
