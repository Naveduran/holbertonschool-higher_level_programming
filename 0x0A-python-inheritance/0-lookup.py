#!/usr/bin/python3
'''
returns the list of available attributes and methods of an object
'''


def lookup(obj):
    '''returns the list of available attributes and methods of an object'''
    attributes = dir(obj)
    return(attributes)
#    variables = [i for i in dir(obj) if not callable(i)]
#    print(variables)
