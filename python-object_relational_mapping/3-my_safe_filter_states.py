#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    matchName = sys.argv[4].split(';')[0].strip("'")

    connection = MySQLdb.connect(
        host="localhost",
        port=3306, user=username,
        passwd=password, db=database,
        charset="utf8")
    crsr = connection.cursor()
    crsr.execute(f"SELECT * FROM states WHERE name LIKE '
                 {matchName}'")
    q_rows = crsr.fetchall()
    for row in q_rows:
        print(row)
    crsr.close()
    connection.close()
