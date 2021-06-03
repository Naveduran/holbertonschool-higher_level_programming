#!/usr/bin/python3
'''module, 11° task'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' inherits from Rectangle'''

    def __init__(self, size):
        '''inicialization of values'''
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        return('[Square] {:d}/{:d}'.format(self.__size, self.__size))
