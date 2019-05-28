#!/usr/bin/python3
"""
funtion to divide a matrix
"""


def matrix_divided(matrix, div):
    """funtion to fivide a matrix"""
    new_list = []
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for x in matrix:
        if len(x) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for y in x:
            if not isinstance(y, (int, float)):
                raise TypeError(msg)
            new_list.append(round(y / div, 2))
    return new_list
