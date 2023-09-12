#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    d = []
    for i in range(n):
        if i == 0:
            d.append([1])
        else:
            temp = []
            for j in range(i + 1):

                if j == 0:
                    temp.append(1)
                elif j < i:
                    temp.append(d[i - 1][j - 1] + d[i - 1][j])
                else:
                    temp.append(d[i - 1][j - 1])
            d.append(temp)
    return(d)
