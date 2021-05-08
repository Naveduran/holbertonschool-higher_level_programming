#!/usr/bin/python3 #squaring a matrix
def common_elements(set_1, set_2):
    common = []
    for i in set_1:
        for e in set_2:
            if i == e:
                common.append(i)
    return common
