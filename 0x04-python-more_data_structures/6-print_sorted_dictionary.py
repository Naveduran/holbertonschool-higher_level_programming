#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    listt = list(a_dictionary.keys())
    listt.sort()
    for val in listt:
        print(val, end='')
        print(":", a_dictionary.get(val))
