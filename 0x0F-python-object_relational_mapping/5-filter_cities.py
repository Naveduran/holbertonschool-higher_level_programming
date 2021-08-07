#!/usr/bin/python3
'''my module 1'''
import MySQLdb
from sys import argv


def Filter_Cities(username, password, db_name, state_name):
    '''receive a city name as argument and list it's cities'''

    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")

    # prepare a cursor object using cursor() method
    cur = db.cursor()

    # execute SQL query using execute() method.
    cur.execute("""SELECT cities.name FROM states
    INNER JOIN cities ON cities.state_id = states.id
    WHERE states.name = %(state_name)s
    ORDER BY cities.id ASC""", {
        'state_name': state_name
    })

    query_rows = cur.fetchall()
    for row in query_rows:
        if query_rows[0] != row:
            print(', ', end='')
        print(row[0], end='')

    print()
    cur.close()


if __name__ == "__main__":
    Filter_Cities(argv[1], argv[2], argv[3], argv[4])
