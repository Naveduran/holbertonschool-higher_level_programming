#!/usr/bin/python3
'''module base '''
import json


class Base():
    '''class Base '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''method init'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''static method that returns the JSON string representation of
        list_dictionaries'''
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)
#            return json(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes the JSON string representation of list_objs to a file '''
        filename = str('{}.json'.format(cls.__name__))
        dict_of_obj = {}
        list_of_dicts = []
        for object in list_objs:
            dict_of_obj = object.to_dictionary()
            list_of_dicts.append(dict_of_obj)
        string = cls.to_json_string(list_of_dicts)
        with open(filename, 'w' ,encoding='utf-8') as file:
            file.write(string)
