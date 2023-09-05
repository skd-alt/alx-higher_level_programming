#!/usr/bin/python3
# 0-add_integer.py
"""An addition of integer function"""


def add_integer(a, b=98):
    """Return the additoion of two integers
        Args:
            a (int or float): number
            b (int or float): number
        if a or b are float they converted to int
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
