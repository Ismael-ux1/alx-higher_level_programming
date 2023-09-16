#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Establishing a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # Creating a cursor object using the cursor() method of the db object
    cur = db.cursor()
    # The query retrieves all records from the states table and
    # sorts them in ascending order by id.
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetching all rows from the last executed SQL statement using the
    # fetchall() method of the cursor object.
    rows = cur.fetchall()
    # Looping through each row in rows. Each row is a tuple where each element
    # corresponds to a field in the record.
    for row in rows:
        print(row)

    # Closing the cursor and database connections using the close()
    # method of the respective objects.
    cur.close()
    db.close()
