#!/usr/bin/python3
"""A function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Function thats write to a file
    Args:
        filename: name of file
        text: text tobe written
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
