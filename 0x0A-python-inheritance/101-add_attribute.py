#!/usr/bin/python3
"""Function that adds an attribute to a class"""


def add_attribute(a_class, attr, value):
    """Sets new attribute in class"""
    if "__dict__" in dir(a_class):
        a_class.__setattr__(attr, value)
    else:
        raise TypeError("can't add new attribute")
