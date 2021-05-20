#!/usr/bin/python3
def magic_string():
    globals()['a'] = 1 if 'a' not in globals() else globals()['a'] + 1
    return 'Holberton, ' * (a - 1) + 'Holberton'
