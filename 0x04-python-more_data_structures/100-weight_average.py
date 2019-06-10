#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if matrix is None or len(matrix) == 0:
        return (0)
    d = 0
    size = len(matrix) - 1
    for a in range(size):
        for b in range(a):
            c = matrix[a] * [b]
            d += matrix[b]
        e += c

    return (e)
