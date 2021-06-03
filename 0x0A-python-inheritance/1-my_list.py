#!/usr/bin/python3
'''a class MyList that inherits from list'''


class MyList(list):
    '''A class that inherits from list type'''

    def print_sorted(self):
        '''a method that prints the sorted list'''

        sorted = self.copy()
        sorted.sort()
        print(sorted)
