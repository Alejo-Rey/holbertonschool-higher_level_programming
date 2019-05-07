#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        w = len(matrix)

        for x in range (w):
            y = len(matrix[x])
            for z in range(y):
                if z < y - 1:
                    print("{:d}".format(matrix[x][z]), end=" ")
                else:
                    print("{:d}".format(matrix[x][z]), end="")
            print()
