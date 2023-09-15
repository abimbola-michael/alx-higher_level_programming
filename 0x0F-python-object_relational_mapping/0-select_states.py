#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """script that lists all states from the database hbtn_0e_0_usa
    """

    con = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    csr = con.cursor()
    csr.execute("SELECT * FROM states")
    rows = csr.fetchall()

    for row in rows:
        print(row)
