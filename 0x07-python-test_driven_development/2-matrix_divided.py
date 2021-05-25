#!/usr/bin/python3
"""
Contains a function that divides all elements of a matrix.

Test by using this command: python3 -m doctest ./tests/*
"""


def matrix_divided(matrix, div):
    '''
    divides all elements of a matrix
    '''
    if type(div) == int or type(div) == float:
        if div == 0:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")

    if matrix == []:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    new_matrix = []
    row_lenght = 0
    listt = []

    for row in matrix:
        if row == []:
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
        row = row.copy()
        if str(row) == str(matrix[0]):
            row_lenght = len(matrix[0])
        else:
            if row_lenght != len(row):
                error = "Each row of the matrix must have the same size"
                raise TypeError(error)

        for item in row:
            if type(item) is not (int or float):
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
            element = float(item / div)
            if element % 1 is 0:
                element = int(element)
            else:
                element = float("{:.2f}".format(element))
            listt.append(element)

        new_matrix.append(listt)
        listt = []

    return new_matrix
