#!/usr/bin/python3
"""A function that writes an Object to a text file, using a JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Write json str to file"""
    with open(filename, "w") as a_file:
        json.dump(my_obj, a_file)
