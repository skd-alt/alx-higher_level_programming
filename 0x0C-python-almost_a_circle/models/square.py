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
        txt = f"[Square] ({self.id}) {self.x}/{self.y} "
        txt += f"- {self.width}"
        return txt
