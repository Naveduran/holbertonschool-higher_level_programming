#!/usr/bin/python3
'''module, 12° task'''


class MyInt(int):
    ''' == and != operators inverted '''

    def __eq__(self, other):
        return(super().__ne__(self))

    def __ne__(self, other):
        return(super().__eq__(self))
