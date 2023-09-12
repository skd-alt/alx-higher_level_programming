#!/usr/bin/python3
"""Creates a Student Class"""


class Student:
    """Student object is created"""
    def __init__(self, first_name, last_name, age):
        """Intializes Student attrs"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return json represention in dictionary"""
        if attrs is None:
            return self.__dict__
        d = {a: self.__getattribute__(a) for a in attrs if a in self.__dict__}
        return d
