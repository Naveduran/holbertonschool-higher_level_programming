#!/usr/bin/python3
'''my module 2'''
import MySQLdb
from sys import argv


def My_Filter_States(username, password, db_name, state_name):
    '''shows only the specified names of states'''

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name,
                         charset="utf8")

    cur = db.cursor()

    cur.execute('SELECT states.id, states.name FROM states WHERE\
    states.name = \'{:s}\' ORDER BY states.id'.format(state_name))

    for row in cur:
        if row[1] == state_name:  # this contional is the senseless key!!!
            print(row)

    cur.close()


if __name__ == "__main__":
    My_Filter_States(argv[1], argv[2], argv[3], argv[4])
