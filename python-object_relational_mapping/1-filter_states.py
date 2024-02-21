#!/usr/bin/python3
"""lists all states with a name sarting with N"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306, user=username,
        passwd=password, db=database,
        charset="utf8")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    q_rows = crsr.fetchall()
    for row in q_rows:
        print(row)
    crsr.close()
    connection.close()
