#!/usr/bin/python3
'''module, 4th task'''


def inherits_from(obj, a_class):
    '''
    returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.
    '''
    if type(obj) != a_class:
        return True
    else:
        return False
#    print(isinstance(type(obj), a_class))
#    print(isinstance(obj.__class__, a_class))
