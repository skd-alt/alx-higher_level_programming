#!/usr/bin/python3
"""A class-checking function if instance of a class that inherited."""


def inherits_from(obj, a_class):
    """Returns True if object is instance of a class that inherited
    Args:
        obj: object being compared
        a_class : class to compare with
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
