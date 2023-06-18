#!/usr/bin/python3
"""
Lists all cities in a state from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        cities.append(str(row[0]))
    print(', '.join(cities))
    cur.close()
    db.close()
