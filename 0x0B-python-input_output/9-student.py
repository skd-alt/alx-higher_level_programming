#!/usr/bin/python3
"""Creates a Student Class"""


class Student:
    """Student object is created"""
    def __init__(self, first_name, last_name, age):
        """Intializes Student attrs"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return json represention in dictionary"""
        return self.__dict__
