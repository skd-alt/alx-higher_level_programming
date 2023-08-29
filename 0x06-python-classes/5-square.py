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
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size

    def area(self):
        """Calculate area of square"""
        return self.__size ** 2

    def my_print(self):
        """print sqaure"""
        for i in range(self.__size):
            print("#" * self.size)
        if self.__size == 0:
            print("")
