#!/usr/bin/python3
'''my module 1'''
import MySQLdb
from sys import argv


def My_Filter_States(username, password, db_name, state_name):
    '''shows only the specified names of states'''

    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")

    # prepare a cursor object using cursor() method
    cur = db.cursor()

    # execute SQL query using execute() method.
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(
        state_name)

    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()


if __name__ == "__main__":
    My_Filter_States(argv[1], argv[2], argv[3], argv[4])
