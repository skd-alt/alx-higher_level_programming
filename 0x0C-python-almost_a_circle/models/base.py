#!/usr/bin/python3
"""Defines a Base model class"""
import json


class Base:
    """Base model class for almost a circle
    Args:
        nb_objects (int): private class attribute
        id (int): public instance attribute to assign id to base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a base class"""
        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
