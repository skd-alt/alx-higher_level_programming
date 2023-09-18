#!/usr/bin/python3i
"""Defines a Base model class"""


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
