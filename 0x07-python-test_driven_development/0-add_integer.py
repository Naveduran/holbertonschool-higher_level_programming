#!/usr/bin/python3
"""
Contains a function that adds 2 integers.
If the second integer is not given it is assigned as 98.
It can receive floats, but it return only the integer part.
The numbers can't be send in string format as 'one'.
They must be numbers.

Test by using this command: python3 -m doctest ./tests/*
"""


def add_integer(a, b=98):
    '''
    adds 2 integers
    '''

    if type(a) != int:
        if type(a) == float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) != int:
        if type(b) == float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    result = a + b
    return result
