#!/usr/bin/python3
"""A Square Class"""


class Square:
    """Square class with Private instance attribute"""

    def __init__(self, size):
        """ Intializes a Square class object

        Note:
            size is a private attribute

        Args:
            size: Lenghth of the square
        """
        self.__size = size
