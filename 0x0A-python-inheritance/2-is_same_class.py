#!/usr/bin/python3
"""A class-checking function."""


def is_same_class(obj, a_class):
    """Returns True if object is the same as a class
    Args:
        obj: object being compared
        a_class : class to compare with
    """

    if type(obj) == a_class:
        return True
    return False

