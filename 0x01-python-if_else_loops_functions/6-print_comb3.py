#!/usr/bin/python3
for a in range(0, 9):
        for b in range(0, 10):
                if a != b and a < b:
                        if a is 8 and b is 9:
                                print("89")
                        else:
                                print("{}{}, ".format(a, b), end='')
