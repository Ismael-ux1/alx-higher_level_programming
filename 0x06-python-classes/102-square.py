#!/usr/bin/python3
"""A class that defines a square by size"""


class Square:
    """A class that defines a square by size"""

    def __init__(self, size=0):
        """Initialize the square with optional size"""
        self.size = size

    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if type(value) not in (int, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare two squares by area for equality"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare two squares by area for inequality"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare two squares by area for less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare two squares by area for less than or equal"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare two squares by area for greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare two squares by area for greater than or equal"""
        return self.area() >= other.area()
