#!/usr/bin/python3
'''
contains a function that prints a indentation with 2 new lines
after each of these characters: ., ? and :
'''


def indentation_indentation(text):
    '''
    function that prints a indentation with 2 new lines
    after each of these characters: ., ? and :
    '''

    if type(text) != str:
        raise TypeError('text must be a string')

    new_text = ''

    for char in text:
        new_text += char
        if char == '?' or char == ':' or char == '.':
            new_text += '\n\n'

    list_of_lines = new_text.split('\n')

    for i in range(len(list_of_lines)):
        if list_of_lines[i].startswith(' ') or list_of_lines[i].endswith(' '):
            list_of_lines[i] = list_of_lines[i].strip(' ')
        if list_of_lines[i] == '\n' and list_of_lines[i + 1] == '\n':
            list_of_lines.pop(i)
            i -= 1

    list_of_lines = list_of_lines[:-1]

    for line in list_of_lines:
        print(line)
