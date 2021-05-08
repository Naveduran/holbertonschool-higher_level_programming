#!/usr/bin/python3 #squaring a matrix
def square_matrix_simple(matrix=[]):
    l = [ele[:] for ele in matrix]
    for i in range(len(l)):
        for e in range(len(l[i])):
            l[i][e] = l[i][e] * l[i][e]
    return l
