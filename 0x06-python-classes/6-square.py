#!/usr/bin/python3
''' an empty class Square that defines a square '''


class Square():
    ''' a square class '''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return(self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__position[1] > 0 or self.__position[0] == 0:
                    None
                else:
                    for k in range(self.__position[0]):
                        print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
