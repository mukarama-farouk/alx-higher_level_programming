#!/usr/bin/python3

"""This module that takes in an argument and displays all values in the state
table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
    )

    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(sys.argv[4]))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    database.close()
