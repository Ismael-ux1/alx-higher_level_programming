#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Defines a MyInt class that inherits from int"""
    def __eq__(self, other):
        """Inverts the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the != operator"""
        return super().__eq__(other)
