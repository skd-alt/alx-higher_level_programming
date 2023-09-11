#!/usr/bin/python3
"""A Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initializes a square of size size.
        Args:
            size (int): The size of square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
