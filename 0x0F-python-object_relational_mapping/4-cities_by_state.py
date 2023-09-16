#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_0_usa.
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to a MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object which allows us to execute SQL commands
    cur = db.cursor()

    # Execute a SQL command to fetch all cities from the 'cities' table
    # The results are sorted in ascending order by 'id'
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                ORDER BY cities.id ASC")

    # Fetch all rows from the last executed SQL command
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)
