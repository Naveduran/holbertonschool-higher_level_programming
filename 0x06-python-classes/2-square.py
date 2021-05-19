#!/usr/bin/python3
''' an empty class Square that defines a square '''


class Square():
    ''' a square class '''
    def __init__(self, size=0):
        try:
            if type(size) == int:
                self.__size = size
            else:
                raise Exception ValueError 
        
