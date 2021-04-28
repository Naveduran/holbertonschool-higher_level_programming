#!/usr/bin/python3
def islower(c):
    c = ord(c)
    for lower in range(97, 123):
        if c is lower:
            return True
    return False
