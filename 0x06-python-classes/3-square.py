#!/usr/bin/python3
"""A class that defines a square."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """
        Constructor method for Square.

        Parameters:
        - size (int): The size of the square.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2
