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
        """Returns the JSON string representation
        Args:
            list_dictionaries (list) : list of dicts
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string to file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as a_file:
            if list_objs is None:
                a_file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                a_file.write(Base.to_json_string(list_dicts))
