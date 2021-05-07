#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    l = len(matrix[0])
    if l < 1:
        print()
    for i in range(l):
        for j in range(l):
            print("{}".format(matrix[i][j]), end=' ')
        print()
