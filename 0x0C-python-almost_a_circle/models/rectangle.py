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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of recatngle"""
        return self.__width * self.__height

    def display(self):
        """ Print the Rectangle #"""
        image = "\n" * self.__y
        image += (" " * self.__x + "#" * self.__width + "\n") * self.__height
        print(image[:-1])

    def update(self, *args, **kwargs):
        """Update attributes"""
        if args is not None and len(args) is not 0:
            list_attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """Return Rectangle attri"""
        txt = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} "
        txt += f"- {self.__width}/{self.__height}"
        return txt
