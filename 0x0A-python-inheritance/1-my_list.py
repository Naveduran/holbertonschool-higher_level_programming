#!/usr/bin/python3
'''a class MyList that inherits from list'''


class MyList(list):

    def print_sorted(self):
        '''a class MyList that inherits from list'''
        sorted = self.copy()
        sorted.sort()
        print(sorted)
