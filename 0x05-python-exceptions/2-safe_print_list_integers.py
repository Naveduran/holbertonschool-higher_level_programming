#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    printed = 0
    suma = 0
    while i < x:
        try:
            suma += int((my_list[i]))
            print("{:d}".format(my_list[i]), end='')
            printed += 1
        except (ValueError, TypeError):
            None
        i = i + 1
    print()

    return printed
