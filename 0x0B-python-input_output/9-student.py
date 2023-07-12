#!/usr/bin/python3
""" A class that defines a student by public instance attribute. """


class Student:
    """
    Class representing a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with the given;
        first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieve a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        json_description = {}

        for attr, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                json_description[attr] = value

        return json_description
