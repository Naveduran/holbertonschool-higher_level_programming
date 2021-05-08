#!/usr/bin/python3 #squaring a matrix
def uniq_add(my_list=[]):
    my_list.sort()
    new = 0
    for i in range(len(my_list)):
        if my_list[i] != my_list[i - 1]:
            new += my_list[i]
    return new
