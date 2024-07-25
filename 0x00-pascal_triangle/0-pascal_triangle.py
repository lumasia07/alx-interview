#!/usr/bin/python3
"""
Pascal triangle module
"""


def pascal_triangle(n):
    """
    Defines a method pascal triangle with (int): n
    """
    if n <= 0:
        return []
    traingle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(traingle[i - 1][j - 1] + traingle[i - 1][j])
        row.append(1)
        traingle.append(row)

    return traingle
