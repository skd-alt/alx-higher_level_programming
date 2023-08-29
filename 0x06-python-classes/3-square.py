#!/usr/bin/python3
"""A Square Class"""


class Square:
    """Square class with Private instance attribute"""

    def __init__(self, size=0):
        """ Intializes a Square class object

        Note:
            size is a private attribute

        Args:
            size: Lenghth of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate area of square"""
        return self.__size ** 2
