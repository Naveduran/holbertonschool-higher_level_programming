#!/usr/bin/python3
'''module rectangle'''
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' class Square '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' class constructor of square '''
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' getter of size '''
        return self.width

    @size.setter
    def size(self, value):
        ''' setter of size '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')  # works
        self.width = value

    def __str__(self):
        ''' return a string '''
        s1 = '[Square] ({}) {}/{} -'.format(self.id, self.x, self.y)
        s2 = ' {}'.format(self.width)
        return s1 + s2

    # FALTA EL PUNTO 12 ARGS Y KWARGS
