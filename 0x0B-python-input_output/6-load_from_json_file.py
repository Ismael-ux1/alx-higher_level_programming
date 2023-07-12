#!/usr/bin/python3
""" A function thaty creates an Object from a JSON file. """

import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The object created from the JSON file.

    Raises:
        None

    Usage:
        obj = load_from_json_file("data.json")
        print(obj)  # Print the object created from the JSON file
    """
    with open(filename, encoding="utf-8") as file:
        obj = json.load(file)
    return obj
