#!/usr/bin/python3
""" Base class to manage ID attribute. """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the JSON string representaion of list_dictionaries. """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))
