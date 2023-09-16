#!/usr/bin/python3
# This is a Python script for listing states starting with 'N' from a database.

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database.
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    # Execute an SQL query.
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'"
                " ORDER BY id ASC")
    # Fetch all rows from the last executed SQL statement.
    rows = cur.fetchall()
    # Print each row.
    for row in rows:
        print(row)
    # Close the cursor and database connections.
    cur.close()
    db.close()
