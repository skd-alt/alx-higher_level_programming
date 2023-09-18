#!/usr/bin/python3
"""Defines a Base model class"""

import json
import csv
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string to file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as a_file:
            if list_objs is None:
                a_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(a_file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """des serialzes a CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as a_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(a_file, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**dicts) for dicts in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        i = -500
        for item in list_rectangles:
            sh = turtle.Turtle()
            sh.penup()
            sh.goto(-i,500)
            sh.goto(item.x - 500, 500 - item.y)
            sh.pendown()
            sh.goto(item.x + item.width - 500, 500 - item.y)
            sh.goto(item.x + item.width - 500, 500 - item.y - item.height)
            sh.goto(item.x - 500, 500 - item.y - item.height)
            sh.goto(item.x - 500, 500 - item.y)
            i += item.height + item.y

        for item in list_squares:
            sh = turtle.Turtle()
            sh.penup()
            sh.goto(-i,500)
            sh.goto(item.x - 500, 500 - item.y)
            sh.pendown()
            sh.goto(item.x + item.size - 500, 500 - item.y)
            sh.goto(item.x + item.size - 500, 500 - item.y - item.size)
            sh.goto(item.x - 500, 500 - item.y - item.size)
            sh.goto(item.x - 500, 500 - item.y)
            i += item.height + item.y

        screen.listen()
        screen.exitonclick()
