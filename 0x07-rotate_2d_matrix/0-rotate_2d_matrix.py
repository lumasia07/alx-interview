#!/usr/bin/python3
"""Rotates a 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate a n * n 90 degrees clockwise"""
    n = len(matrix)
    for x in range(n):
        for y in range(x, n):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    for _ in range(n):
        matrix[_].reverse()
