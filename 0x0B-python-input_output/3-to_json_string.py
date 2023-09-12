#!/usr/bin/python3
"""A function that returns the JSON representation"""
import json


def to_json_string(my_obj):
    """Jsonify an object"""
    return json.dumps(my_obj)
