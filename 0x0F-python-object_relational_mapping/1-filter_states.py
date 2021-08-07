#!/usr/bin/python3
"""my module 1"""
import MySQLdb
from sys import argv


def Filter_States(username, password, db_name):
    """lists all states with a name starting with N"""

    # Open database connection
    db = MySQLdb.connect(user=username,
                         passwd=password,
                         db=db_name)

    # prepare a cursor object using cursor() method
    cur = db.cursor()

    # execute SQL query using execute() method.
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # close cursor and connection
    cur.close()
    db.close()


if __name__ == "__main__":
    Filter_States(argv[1], argv[2], argv[3])
