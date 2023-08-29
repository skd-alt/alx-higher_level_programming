#!/usr/bin/python3
"""A Square Class"""


class Square:
    """Square class with Private instance attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """ Intializes a Square class object

        Note:
            size is a private attribute

        Args:
            size: Lenghth of the square
            position: position to print
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """get size value"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get position value"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate area of square"""
        return self.__size ** 2

    def my_print(self):
        """print sqaure"""
        if self.__size == 0:
            print("")
        if self.__position[1] > 0:
            print("\n" * self.__position[1])
        for i in range(self.__size):
            if self.__size > 0:
                print(" " * self.__position[0] + "#" * self.size)
