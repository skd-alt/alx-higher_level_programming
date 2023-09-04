#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """Represent a rectangle.
    Attributes:
        number of instances to set dimensions of rectangle
        print_symbol set symbol
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing the dimesions of the rectangle
        args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            number_of_instances (int): current number
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        image = (str(self.print_symbol) * self.__width + "\n") * self.__height
        return image[:-1]

    def __repr__(self):
        """print() or eval() __repr__ method function"""
        w = str(self.__width)
        h = str(self.height)
        repr_string = "Rectangle(" + w + ", " + h + ")"
        return repr_string

    def __del__(self):
        """Deletes instance of Rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares to rectangles area
            Args:
                rect_1: fist rectangle
                rect_2: second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
