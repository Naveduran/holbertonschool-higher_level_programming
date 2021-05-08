#!/usr/bin/python3 #squaring a matrix
def only_diff_elements(set_1, set_2):
    diff = list(set_1) + list(set_2)
    diff.sort()
    for i in range(len(diff) - 3):
        if diff[i] == diff[i + 1]:
            diff.remove(diff[i + 1])
            diff.remove(diff[i])
    return diff
