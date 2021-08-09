#!/usr/bin/python3
"""my module 1"""
import MySQLdb
from sys import argv


def Filter_States(username, password, db_name):
    """lists all states with a name starting with N"""

    db = MySQLdb.connect(user=username,
                         passwd=password,
                         db=db_name)

    cur = db.cursor()

    cur.execute("SELECT states.id, states.name FROM states WHERE\
        name LIKE 'N%' ORDER BY states.id ASC;")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    Filter_States(argv[1], argv[2], argv[3])
