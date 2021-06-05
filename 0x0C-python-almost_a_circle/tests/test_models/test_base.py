#!/usr/bin/python3
'''unit test for base and its functions'''
import os
import unittest
from models.base import Base


class TestFunction(unittest.TestCase):
    '''unit test for class Base'''

    word = "Betty"
    string = "Betty Holberton"
    pharagraph = '''Lorem Ipsum is simply dummy text of the printing and\
        typesetting industry. Lorem Ipsum has been the	industry's standard\
        dummy text ever since the 1500s, when an unknown printer took a galley\
        of type and scrambled it to make a type specimen book. It has survived\
        not only five centuries, but also the leap into electronic typesetting\
        ,remaining essentially unchanged. It was popularised in the 1960s with\
        the release of Letraset sheets containing Lorem Ipsum passages, and\
        more recently with desktop publishing software like Aldus PageMaker\
        including versions of Lorem Ipsum.'''
    positive = 5
    negatve = -5
    zero = 0
    nothing = None
    dictionary = {'Key0': 0, 'Key1': 1, 'Key2': 2, 'Key3': 2, 'Key4': 3, }
    list = [1, 2, 3, 4, 5]
    boolean = True

    def test_function(self):
        '''test for function___'''

        # files are executable

        assertTrue(os.access('./models/base.py', os.X_OK))

        # pep8

        assertTrue(os.system('pep8 --count base.py'))

        # documentation of classes and functions

        assertTrue(os.system(len('base'.__doc__) > 10))
        assertTrue(os.system(len(Base.__doc__) > 10))

        # first and last line

        with open('base.py') as f:
            first = f.read()[-1]
            last = f.readline()

        assertTrue(first == '\n\n')
        assertTrue(last == '#!/usr/bin/python3\n')

        # base has a private attribute __nb_objects and its equal to 0

        assertTrue(__nb_objects in dir(Base))

        # base has a method __init__(self, id=None)

        assertTrue(__init__ in dir(Base))

        # __init(none) => nb += 1, public_id = nb

        # __init(!=none) => public_id = id

        u = base()
        assertTrue(u.__nb_objects, 0)
        u.id

    def test_raise_errors(self):
        '''test output for different type of input values'''
        assertRaises(ValueError, function, arg)


# base has a method to_json_string(list_dictionaries)
# to_json_string devuelve un string

# base has a static method from_json_string(json_string)
# from_json_string devuelve una lista

# base has a class method create(cls, **dictionary)
# returns an object with all the attributes setted

# base has a class method load_from_file(cls)
# returns a list of instances

# ___
# base has a class method save_to_file_csv(cls, list_objs)
# do

# base has a class method load_from_file_csv(cls):
# do


'''
assertTrue(x)
assertFalse(x)
assertIs(a, b)
assertIsNot(a, b)
assertIn(a, b)
assertNotIn(a, b)
assertIsInstance(a, b)
assertNotIsInstance(a, b)
'''
