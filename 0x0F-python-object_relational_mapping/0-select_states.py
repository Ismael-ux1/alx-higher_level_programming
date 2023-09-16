#!/usr/bin/python3
# A script that lists all states from the database hbtn_0e_0_usa:
import MySQLdb
import sys


def list_states(username, password, database_name):
    try:
        # Connect to MySQL server
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name,
            charset="utf8"
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Execute SQL query to fetch states in ascending order by states.id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        username, password, database_name = sys.argv[1:4]
        list_states(username, password, database_name)
