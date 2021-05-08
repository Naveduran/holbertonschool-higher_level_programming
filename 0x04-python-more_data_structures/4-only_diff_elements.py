#!/usr/bin/python3 #squaring a matrix
def only_diff_elements(set_1, set_2):
    diff = list(set_1) + list(set_2)
    diff.sort()
    i = 0
    c = len(diff) - 1
    while(i < c):
        if diff[i] == diff[i + 1]:
            diff.remove(diff[i + 1])
            diff.remove(diff[i])
            c = c - 2
            i = 0
        else:
            i = i + 1
    return diff
