#!/usr/bin/python3
''' a module for read a file'''


def read_file(filename=""):
    '''a function to read a file'''
    with open(filename, encoding="utf-8") as file:
        readed = file.read()
        if readed == '':
            raise Exception('file is empty')
        print(readed, end='')
