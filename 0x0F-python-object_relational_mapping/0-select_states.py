#!/usr/bin/python3
'''my module 0'''
import MySQLdb
from sys import argv


def Get_States(username, password, db_name):
    '''a script that lists all states from the database hbtn_0e_0_usa'''

    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")

    # prepare a cursor object using cursor() method
    cur = db.cursor()

    # execute SQL query using execute() method.

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

        # close cursor and connection
        cur.close()
#       db.close()


if __name__ == "__main__":
    Get_States(argv[1], argv[2], argv[3])
