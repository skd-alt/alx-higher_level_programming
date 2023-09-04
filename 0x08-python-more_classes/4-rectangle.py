#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """Represent a rectangle.
    Attributes:
        number of instances to set dimensions of rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializing the dimesions of the rectangle
        args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the recatngle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter if eitherf side is not 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.width + self.__height) * 2

    def __str__(self):
        """ Return the Rectangle #"""
        image = ""
        if self.__width == 0 or self.__height == 0:
            return image
        image = ("#" * self.__width + "\n") * self.__height
        return image[:-1]

    def __repr__(self):
        """print() or eval() __repr__ method function to create a new function"""
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
