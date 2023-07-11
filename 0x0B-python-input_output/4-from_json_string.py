#!/usr/bin/python3
""" A function that returns an object represented by JSON string. """

import json


def from_json_string(my_str):
    """
    Return a Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string representing the object.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    obj = json.loads(my_str)
    return obj
