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

    # start with triangle, a list of list
    triangle = [[1]]

    # for each row number  from 1 to n -1  start with 1
    for row in range(1, n):
        new_row = [1]

        # calculate middle element
        # for each element index from 1 to
        # (length of previous row - 1):
        for i in range(1, len(triangle[row - 1])):
            new_element = triangle[row - 1][i - 1] + triangle[row - 1][i]
            new_row.append(new_element)

        new_row.append(1)  # end the row with 1
        triangle.append(new_row)

    return triangle
