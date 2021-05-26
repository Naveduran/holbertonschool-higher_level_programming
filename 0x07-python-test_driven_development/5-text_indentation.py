#!/usr/bin/python3
'''
contains a function that prints a text with 2 new lines
after each of these characters: ., ? and :
'''


def text_indentation(text):
    '''
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    '''

    if type(text) != str:
        raise TypeError('text must be a string')

    text = text.strip()
    new_text = ''

    for char in text:
        if char != '\n':
            new_text += char
        if char == '?' or char == ':' or char == '.':
            new_text += '\n'

    list_of_lines = new_text.split('\n')

    new_list = []

    for line in list_of_lines:
        if line != '':
            item = line.strip(' ')
            print(item, end='')
            last_c = item[-1]
            if last_c == '?' or last_c == ':' or last_c == '.':
                print('\n')
