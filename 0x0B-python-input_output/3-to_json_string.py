#!/usr/bin/python3
""" A function that returns the JSON representation of an object(string). """

import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object as string.

    Args:
        my_obj: The object to be serialized into JSON.

    Returns:
        str: The JSON representation of the object as a string.
    """
    json_string = json.dumps(my_obj)
    return json_string
