#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Args:
        n (int): size of triangle
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    d = []
    for i in range(n):
        temp = []
        for j in range(i + 1):

            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(d[i - 1][j - 1] + d[i - 1][j])
        d.append(temp)
    return(d)
