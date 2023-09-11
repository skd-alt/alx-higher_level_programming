#!/usr/bin/python3
"""A instance-checking function."""


def is_kind_of_class(obj, a_class):
    """Returns True if object is an instance of a class
    Args:
        obj: object being compared
        a_class : class to compare with
    """

    if isinstance(obj, a_class):
        return True
    return False
