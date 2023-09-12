#!/usr/bin/python3
"""Recreate Python Object form json file"""
import json


def load_from_json_file(filename):
    """Creat Python Object fro JSON file"""
    with open(filename) as a_file:
        return json.load(a_file)
