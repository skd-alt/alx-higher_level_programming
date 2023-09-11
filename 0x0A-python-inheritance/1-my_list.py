#!/usr/bin/python3
# 1-my_list.py
"""Define a MyList class"""


class MyList(list):
    """MyList class that inherits from the list class"""

    def print_sorted(self):
        """sorts a list"""
        print(sorted(self))
