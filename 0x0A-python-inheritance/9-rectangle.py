#!/usr/bin/python3
"""Defines a Rectangle Class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Classs rectangle is defined."""

    def __init__(self, width, height):
        """initialization function
        Args:
            width: base width of rectangle
            heigth: height of a rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate the aera of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """str representatio of function"""
        s = "[" + str(self.__class__.__name__) + "]"
        s += " " + str(self.__width) + "/" + str(self.__height)
        return s
