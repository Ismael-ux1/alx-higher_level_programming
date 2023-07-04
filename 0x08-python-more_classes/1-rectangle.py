#!/usr/bin/python3
"""Defines the a Rectangle Object."""


class Rectangle:
    def __init__(self, width=0, height=0):
        # Initialize the Rectangle object with the provided width and height
        self._width = width
        self._height = height

    @property
    def width(self):
        # Getter method for retrieving the width of the rectangle
        return self._width

    @width.setter
    def width(self, value):
        # Setter method for setting the width of the rectangle
        self._width = value

    @property
    def height(self):
        # Getter method for retrieving the height of the rectangle
        return self._height

    @height.setter
    def height(self, value):
        # Setter method for setting the height of the rectangle
        self._height = value

    def __repr__(self):
        # Return a string representation of the rectangle object
        return f"Rectangle(width={self._width}, height={self._height})"

