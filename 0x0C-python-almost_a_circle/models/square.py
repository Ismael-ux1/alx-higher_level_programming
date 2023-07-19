#!/usr/bin/python3
from models.rectangle import Rectangle
""" Class Square inherits from Rectangle. """


class Square(Rectangle):
    """ Class square inherits from Rectangle. """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initalize Square instance. """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of square instance. """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
