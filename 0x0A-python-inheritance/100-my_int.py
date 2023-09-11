#!/usr/bin/python3
"""A class MyInt inherits from Int"""


class MyInt(int):
    """MyInt class defined"""

    def __eq__(self, other):
        """equals defined as not equal"""
        if self.__int__() == other.__int__():
            return False
        else:
            return True

    def __ne__(self, other):
        """Not equal defined as equal"""
        if self.__int__() == other.__int__():
            return True
        else:
            return False
