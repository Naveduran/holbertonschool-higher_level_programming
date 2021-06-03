#!/usr/bin/python3
'''a class MyList that inherits from list'''


class MyList(list):
    '''MyList is a  class that inherits from list type'''
    def print_sorted(self):
        '''Print sorted is a method that prints the sorted list'''
        print(sorted(self))
