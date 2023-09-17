#!/usr/bin/python3
"""a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """a script that takes in an argument and displays all
    values in the states
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
            "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
            )
    rows = crs.fetchall()
    for row in rows:
        print(row)
    crs.close()
    con.close()
