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
    def size(self, new_size):
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size

    @property
    def position(self):
        """get position value"""
        return self.__position

    @position.setter
    def position(self, new_position):
        if not isinstance(new_position, tuple) or len(new_position) != 2 or not all(isinstance(num, int) for num in new_position) or not all(num >= 0 for num in new_position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = new_position

    def area(self):
        """Calculate area of square"""
        return self.__size ** 2

    def my_print(self):
        """print sqaure"""
        if self.__position[1] > 0:
            print("\n" * self.__position[1])
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.size)
        if self.__size == 0:
            print("")
