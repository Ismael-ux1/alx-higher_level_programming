#!/usr/bin/python3
""" A a class Student that defines a student by Public instance attributes. """


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

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): A list of attribute names to be retrieved.

        Returns:
            dict: A dictionary representation of the Student instance.

        Notes:
            If attrs is a list of strings,
            only attribute names contained in this list will be retrieved.
            Otherwise, all attributes will be retrieved.
        """
        if attrs is None:
            attrs = self.__dict__.keys()
        else:
            attrs = set(attrs)

        json_description = {}

        for attr, value in self.__dict__.items():
            if attr in attrs and \
                    isinstance(value, (list, dict, str, int, bool)):
                json_description[attr] = value

        return json_description
