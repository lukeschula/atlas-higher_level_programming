#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities"""

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
    crsr.execute("SELECT c.name \
                FROM cities AS c \
                JOIN states AS st \
                    ON c.state_id = st.id \
                WHERE st.name = '{}' ORDER BY c.id".format(matchName))
    q_rows = crsr.fetchall()
    complete = 0
    for row in q_rows:
        if complete > 0:
            print(", ", end="")
        print(row[0], end="")
        complete += 1
    print()
    crsr.close()
    connection.close()
