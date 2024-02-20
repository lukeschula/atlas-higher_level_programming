#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa"""


from sys import argv
import MySQLdb

if __name__ == '__main__':
    data_b = MySQLdb.connect(host="localhost", port=3306, user=argv[1]
                             psswd=argv[2], data_b=argv[3], charset="utf-8")
    crsr = data_b.crsr()
    sql = "SELECT * FROM states ORDER BY states.id ASC"
    crsr.execute(sql)
    q_rows = crsr.fetchall()

    for row in q_rows:
        print(row)
    crsr.close()
    data_b.close