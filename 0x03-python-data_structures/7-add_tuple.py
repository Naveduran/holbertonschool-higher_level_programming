#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        y = 0
        if len(tuple_a) == 1:
            y = tuple_a[0]
        tuple_a = ((y), 0)
    if len(tuple_b) < 2:
        y = 0
        if len(tuple_b) == 1:
            y = tuple_b[0]
        tuple_b = ((y), 0)
    c = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return c