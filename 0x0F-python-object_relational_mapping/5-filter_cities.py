#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa.
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
    # Where the state name matches the user input
    # The %s placeholder is used to avoid SQL injection attacks
    cur.execute("SELECT cities.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))

    # Fetch all rows from the last executed SQL command
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row[0], end=", ")

    # Close the cursor and database connections
    cur.close()
    db.close()
