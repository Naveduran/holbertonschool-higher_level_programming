#!/usr/bin/python3
'''module, 11° task'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' inherits from Rectangle'''

    def __init__(self, size):
        '''inicialization of values'''
        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size)
