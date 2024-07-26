#!/usr/bin/python3
"""Implementing the Pascal's Triangle"""


def pascal_triangle(n):
    """Generates the pascal triangle for n rows

    Args:
        n (int): A positive integer
    """
    if not isinstance(n, int):
        return []

    if n <= 0:
        return []

    triangle = [[1]]

    for row in range(1, n):
        new_row = [1]

        # calculate middle element
        for i in range(1, len(triangle[row - 1])):
            new_element = triangle[row - 1][i - 1] + triangle[row - 1][i]
            new_row.append(new_element)

        new_row.append(1)  # end the row with 1
        triangle.append(new_row)

    return triangle
