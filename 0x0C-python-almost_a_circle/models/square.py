#!/usr/bin/python3
""" Class Square inherits from Rectangle. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class square inherits from Rectangle. """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initalize Square instance. """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of square instance. """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assign attributes to the instance. """
        if args and len(args) > 0:
            # Update attributes using *args
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        else:
            # Update attributes using **kwargs
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Return the dictionary representation of a Square. """
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
            }
