#!/usr/bin/python3
# unit test for base.py script and requirements of the general proyect

import unittest  # allows to assert
import os  # allows to run bash commands

# scripts to test:
from models.base import Base
from models.rectangle import Rectangle
# from models.square import Square


class Test_Base(unittest.TestCase):
    # class to test the unit models.base.py

    word = 'Betty'
    string = 'Betty Holberton'
    positive = 5
    negatve = 0 - 5
    zero = 0
    nothing = None
    dictionary = {'Key0': 0, 'Key1': 1, 'Key2': 2, 'Key3': 3, 'Key4': 4}
    list = [1, 2, 3, 4, 5]
    boolean = True

    def test_Base(self):
        # test for class Base, task 0

        a = Base()
# ?        self.assertEqual(a.__nb_objects, 1)
        b = Base()
        c = Base()
        d = Base(12)
        e = Base()

        self.assertEqual(a.id, 1)
        self.assertEqual(b.id, 2)
        self.assertEqual(c.id, 3)
        self.assertEqual(d.id, 12)
        self.assertEqual(e.id, 4)
# ?        self.assertEqual(__nb_objects, 4)

        self.assertTrue(type(a), Base)
        self.assertIsInstance(a, Base)

    def doc_of_funcs(self):

        # documentation of functions

        # base has a method to_json_string(list_dictionaries)
        # to_json_string devuelve un string

        # base has a static method from_json_string(json_string)
        # from_json_string devuelve una lista

        # base has a class method create(cls, **dictionary)
        # returns an object with all the attributes setted

        # base has a class method load_from_file(cls)
        # returns a list of instances

        # base has a class method save_to_file_csv(cls, list_objs)
        # do

        # base has a class method load_from_file_csv(cls):
        # do

        pass

    def whole_project_requirements(self):

        # existence of all files and directories in the correct location

        self.assertTrue(os.path.isfile('README.md'))

        self.assertTrue(os.path.isdir('models'))

        self.assertTrue(os.path.isfile('./models/__init__.py'))
        self.assertTrue(os.path.isfile('./models/base.py'))
        self.assertTrue(os.path.isfile('./models/rectangle.py'))
        self.assertTrue(os.path.isfile('./models/square.py'))

        self.assertTrue(os.path.isdir('tests'))
        self.assertTrue(os.path.isdir('./tests/test_models'))

        self.assertTrue(os.path.isfile('./tests/test_models/__init__.py'))
        self.assertTrue(os.path.isfile('./tests/test_models/test_base.py'))
        # self.assertTrue(os.path.isfile('./tests/test_models/test_rectangle.py'))
        # self.assertTrue(os.path.isfile('./tests/test_models/test_square.py'))

        # files are executable
        self.assertTrue(os.access('./models/base.py', os.X_OK))
        self.assertTrue(os.access('./models/rectangle.py', os.X_OK))
        self.assertTrue(os.access('./models/square.py', os.X_OK))

        # first and last line OF BASE
        with open('./models/base.py') as f:
            first = f.readline()
            last = f.read()[-1]

        self.assertTrue(first == '#!/usr/bin/python3\n')
        self.assertTrue(last == '\n')

        # pep8
        self.assertEqual(os.system('pep8 --count ./models/base.py'), 0)
        self.assertEqual(os.system('pep8 --count ./models/rectangle.py'), 0)
        self.assertEqual(os.system('pep8 --count ./models/square.py'), 0)

        # documentation of modules and classes
        self.assertTrue(len('base'.__doc__) > 8)
        self.assertTrue(len(Base.__doc__) > 8)

        self.assertTrue(len('rectangle'.__doc__) > 8)
        self.assertTrue(len(Rectangle.__doc__) > 8)

        # self.assertTrue(len('square'.__doc__) > 8)
        # self.assertTrue(len(Square.__doc__) > 8)


if __name__ == '__main__':
    unittest.main()
