#!/usr/bin/python3
"""This module takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""

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
    cur = database.cursor()
    sname = sys.argv[4]
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sname,))

    cities = cur.fetchall()
    tmp = list(city[0] for city in cities)
    print(*tmp, sep=", ")

    cur.close()
    database.close()
