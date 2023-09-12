#!/usr/bin/python3
"""A function that returns an object from json"""
import json


def from_json_string(my_str):
    """Json to Python object"""
    return json.loads(my_str)
