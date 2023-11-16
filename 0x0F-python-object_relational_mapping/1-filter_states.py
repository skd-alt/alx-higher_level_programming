#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(
            host="localhost", port=3360, user=argv[1],
            passwd=argv[2], db=argv[3], charset="utf8"
            )

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    states = cur.fetchall()
    for state in states:
        print(state)
