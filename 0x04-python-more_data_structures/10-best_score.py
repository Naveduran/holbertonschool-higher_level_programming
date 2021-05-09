#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        c = 0
        for key, value in a_dictionary.items():
            if value > c:
                c = value
                y = key
        return y
    return None
