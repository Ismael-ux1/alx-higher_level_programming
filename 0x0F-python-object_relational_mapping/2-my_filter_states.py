#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states,
table of hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to a MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object which allows us to execute SQL commands
    cur = db.cursor()

    # Execute a SQL command to fetch all states
    # where the name matches the user input
    cur.execute(
            "SELECT * FROM states "
            "WHERE name = %s "
            "ORDER BY states.id ASC",
            (sys.argv[4],)
            )

    # Fetch all rows from the last executed SQL command
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connections
    cur.close()
    db.close()
