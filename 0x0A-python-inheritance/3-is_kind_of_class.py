#!/usr/bin/python3
""" A function that Check if an object is an instance of a specified class or its subclass. """


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of a_class or  its subclass.

    Args:
      obj: The object to check.
      a_class: The class to check against.

    Returns:
       True if obj is instance of a_class or its subclass, otherwise False.
    """
    return isinstance(obj, a_class)
