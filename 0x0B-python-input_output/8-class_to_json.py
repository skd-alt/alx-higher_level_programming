#!/usr/bin/python3
"""
A function that returns the dictionary
description with simple data structure
"""


def class_to_json(obj):
    """Return json representation"""
    return obj.__dict__
