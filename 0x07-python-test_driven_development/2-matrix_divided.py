#!/usr/bin/python3
""" This module defines a matrix division function """


def matrix_divided(matrix, div):
    """
    Divide each elemnet of the matrix by divisor.

    Args:
        matrix: A matrix represented as a list of lists of intgers/floats
        div (int or float): The divisor.

    Returns:
      list: A new matrix where each element is the result of dividingelement

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
         ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row has the same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]

    return new_matrix
