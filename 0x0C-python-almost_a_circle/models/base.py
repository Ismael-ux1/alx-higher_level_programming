#!/usr/bin/python3
""" Base class to manage ID attribute. """
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            # Create a dummy instance
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            # Create a dummy instance
            new_instance = cls(1)

        # Apply the real values using update method
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            # Create a dummy instance of Rectangle
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            # Create a dummy instance of a Square
            dummy_instance = cls(1)
        else:
            return None
        # Update the dummy instance with attributes from dictionary
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
        except FileNotFoundError:
            return []

        list_dicts = Base.from_json_string(json_data)
        instances_list = []
        for dictionary in list_dicts:
            instance = cls.create(**dictionary)
            instances_list.append(instance)
        return instances_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                    elif cls.__name__ == "Square":
                        row = [obj.id, obj.size, obj.x, obj.y]
                    writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", newline="") as file:
                reader = csv.reader(file)
                list_objs = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dict = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        }
                    elif cls.__name__ == "Square":
                        dict = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        }
                    list_objs.append(cls.create(**dict))
                return list_objs
        except FileNotFoundError:
            return []
