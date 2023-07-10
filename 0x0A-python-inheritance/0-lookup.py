#!/usr/bin/python3
""" A function that return a list """


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
         obj: The object to inspect.

    Returns:
         A list that represents available attributes and methods of the object.
    """
    return dir(obj)
