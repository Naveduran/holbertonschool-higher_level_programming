#!/usr/bin/python3
'''module 2 task'''


def is_same_class(obj, a_class):
    '''
    function that returns True if the object is exactly an
    instance of the specified class ; otherwise False
    '''
    if type(obj) == a_class:
        return True
    else:
        return False
#    print(type(obj))
#    print(a_class)
#    print(isinstance(obj, a_class))
#    print(issubclass(obj, a_class))
