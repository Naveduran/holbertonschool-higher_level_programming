#!/usr/bin/python3
"""my module 1"""
import MySQLdb
from sys import argv


def Filter_States(username, password, db_name):
    """lists all states with a name starting with N"""

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name,
                         charset="utf8")

    cur = db.cursor()

    cur.execute("SELECT states.id, states.name FROM states WHERE\
        ASCII(states.name) = 78 ORDER BY states.id;")

    query = cur.fetchall()

    for row in query:
        print(row)

    cur.close()


if __name__ == "__main__":
    Filter_States(argv[1], argv[2], argv[3])
