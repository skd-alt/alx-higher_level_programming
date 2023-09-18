#!/usr/bin/python3
"""
    Class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Defines the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        self.__height = value

    @property
    def x(self):
        """Gets the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x"""
        self.__x = value

    @property
    def y(self):
        """Gets the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y"""
        self.__y = value
