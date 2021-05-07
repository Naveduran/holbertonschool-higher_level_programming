#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    l = len(matrix[0])
    m = len(matrix)
    for i in range(m):
        for j in range(l):
            print("{:d}".format(matrix[i][j]), end='')
            if j != l - 1:
                print("", end=" ")
        print()
