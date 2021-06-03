#!/usr/bin/python3
'''A function to add an attribute'''


def add_attribute(obj, attribute, value):
    '''A function to add an attribute'''
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
