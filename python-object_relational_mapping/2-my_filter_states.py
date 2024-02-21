#!/usr/bin/python3
"""takes in an argument and displays all values in the states table"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    matchName = sys.argv[4]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306, user=username,
        passwd=password, db=database,
        charset="utf8")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM states WHERE name LIKE binary '{}'"
                .format(matchName))
    q_rows = crsr.fetchall()
    for row in q_rows:
        print(row)
    crsr.close()
    connection.close()
