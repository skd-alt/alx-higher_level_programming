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

    @staticmethod
    def from_json_string(json_string):
        """Return the json string to object"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates an instance of a class. """
        if cls.__name__ == "Rectangle":
            new = cls(1, 2)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            a_file = open(filename, "r")
        except IOError:
            return []
        else:
            list_dicts = Base.from_json_string(a_file.read())
            return [cls.create(**dicts) for dicts in list_dicts]
