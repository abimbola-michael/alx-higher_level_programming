#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """a script that lists all cities from the database hbtn_0e_4_usa
    """
    con = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    crs = con.cursor()
    crs.execute(
            "SELECT cities.id, cities.name, states.name FROM cities\
                     INNER JOIN states ON states.id=cities.state_id"
            )
    rows = crs.fetchall()
    for row in rows:
        print(row)
    crs.close()
    con.close()
