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
    cur.execute("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id;")

    cities = cur.fetchall()

    for city in cities:
        print(city)
