#!/usr/bin/python3
"""A text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string.
    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as a_file:
        for line in a_file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w_file:
        w_file.write(text)
