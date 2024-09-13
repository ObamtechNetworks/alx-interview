#!/usr/bin/python3
"""
Module for rotating a 2D matrix by 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in place.

    :param matrix: List of lists representing the 2D matrix
    :return: Nothing, the matrix is modified in place
    """
    # Step 1: Transpose the matrix (swap rows and columns)
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            # Swap matrix[i][j] with matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row to achieve the 90-degree clockwise rotation
    for i in range(n):
        matrix[i].reverse()
