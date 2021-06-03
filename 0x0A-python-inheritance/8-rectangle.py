#!/usr/bin/python3
'''module, 8° task'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle inherits from BaseGeometry'''

    def __init__(self, width, height):
        '''inicialization of values'''
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
