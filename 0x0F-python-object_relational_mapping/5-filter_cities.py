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
    cur.execute("SELECT cities.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            WHERE states.name = '{}';".format(argv[4]))

    cities = cur.fetchall()

    print(", ".join([city[0] for city in cities]))
