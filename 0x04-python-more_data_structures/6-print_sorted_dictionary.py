#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    listt = list(a_dictionary.keys())
    listt.sort()
    dic = {}
    for key in sorted(a_dictionary):
        print(key + ": " + str(a_dictionary.get(key)))
