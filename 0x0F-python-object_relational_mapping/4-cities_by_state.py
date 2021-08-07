#!/usr/bin/python3
'''my module 1'''
import MySQLdb
from sys import argv


def My_Safe_Filter(username, password, db_name):
    '''safe sql query'''

    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")

    # prepare a cursor object using cursor() method
    cur = db.cursor()

    # execute SQL query using execute() method.
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM states
    INNER JOIN cities ON cities.state_id = states.id
    ORDER BY cities.id ASC""")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()


if __name__ == "__main__":
    My_Safe_Filter(argv[1], argv[2], argv[3])
