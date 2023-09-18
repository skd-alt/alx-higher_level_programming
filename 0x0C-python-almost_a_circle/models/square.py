#!/usr/bin/python3
"""
    Class Square inherits from Rectangle and base
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """intializes rectangle as a sqaure"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return Square attributes"""
        txt2 = f"[Square] ({self.id}) {self.x}/{self.y} "
        txt2 += f"- {self.width}"
        return txt2

    @property
    def size(self):
        """Gets the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of sqaure"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes"""
        if args is not None and len(args) is not 0:
            list_attrs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary of values"""
        dict_square = {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
        return dict_square
