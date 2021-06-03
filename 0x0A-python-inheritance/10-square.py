#!/usr/bin/python3
'''module, 10° task'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' inherits from Rectangle'''
    def __init__(self, size):
        '''inicialization of values'''
        self.__size = size
        self.integer_validator('width', size)
        super().__init__(size, size)
