#!/usr/bin/python3
"""A function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """ A function that appends
    Args:
        filename: name of file
        text: text tobe written
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
