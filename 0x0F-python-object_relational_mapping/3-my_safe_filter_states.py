#!/usr/bin/python3

"""This module takes in arguments and displays all values in
the states table of hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )
    cursor = database.cursor()
    sname = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (sname, ))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    database.close()
