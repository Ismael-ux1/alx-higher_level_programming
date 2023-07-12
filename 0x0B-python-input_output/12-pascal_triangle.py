#!/usr/bin/python3
""" A function that returns a list of lists of integers """


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows to generate in the pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    Raises:
         None.
    """
    if n <= 0:
        return []

    triangle = []
    for row in range(n):
        current_row = []
        for index in range(row + 1):
            if index == 0 or index == row:
                current_row.append(1)
            else:
                element = triangle[row-1][index] + triangle[row-1][index-1]
                current_row.append(element)
        triangle.append(current_row)

    return triangle
