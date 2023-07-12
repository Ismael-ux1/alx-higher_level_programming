#!/usr/bin/python3
""" A function that writes an Object to a text file, using a JSON. """

import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized and saved to the file.
        filename (str): The name of the text file to be created or overwritten.

    Returns:
    None
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file, ensure_ascii=False)
