#!/usr/bin/python3
""" A function that returns the dictionary description. """


def class_to_json(obj):
    """
    Return a dictionary description with;
    a simple data structure for JSON serialization of an object.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary description of the object;
        with a simple data structure for JSON serialization.

     Raises:
        None
    """
    json_description = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_description[key] = value

    return json_description
