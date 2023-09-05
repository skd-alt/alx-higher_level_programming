#!/usr/bin/python3
# 4-print_square.py
"""Print Square"""


def print_square(size):
    """ Print a sqaure of size size

    Args:
        size (int) : size of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        pass
    if size > 0:
        print((("#" * size + "\n") * size)[:-1])
