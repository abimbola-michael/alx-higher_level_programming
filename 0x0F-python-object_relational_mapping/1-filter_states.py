#!/usr/bin/python3
""" a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """a script that lists all states with a name starting with N
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
            """SELECT * FROM states WHERE name
             LIKE BINARY 'N%' ORDER BY states.id"""
            )
    rows = crs.fetchall()
    for row in rows:
        print(row)
    crs.close()
    con.close()
