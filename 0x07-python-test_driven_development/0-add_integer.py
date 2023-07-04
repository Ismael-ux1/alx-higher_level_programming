#!/usr/bin/python3
"""
This function adds two integers.

Args:
    a (int, float): The fist integer or float to add.
    b (int, float): The second integer or float to add. Default is 98.

Returns:
    int: The sum of a and b as an integer.

Raises:
    TypeError: If either a or b is not an integer or float.
"""


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
