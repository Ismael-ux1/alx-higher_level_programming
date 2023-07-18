#!/usr/bin/python3
""" Base class to manage ID attribute. """


class Base:
    """
    Base class to manage ID attribute.

    Attributes:
        __nb_objects (int): Private class attribute for tracking object count.
        id (int): Public instance attribute representing the object ID.

    Methods:
        __init__(self, id=None): Initialize a new instance of the Base class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of Base.

        Args:
             id (int) : ID value for the object.

        Notes:
           - if id is not provided, a unique ID is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
