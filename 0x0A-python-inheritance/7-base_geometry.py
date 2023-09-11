#!/usr/bin/python3
"""An class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry Class"""

    def area(self):
        """Raise Exception when run"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function tha validates the value"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
