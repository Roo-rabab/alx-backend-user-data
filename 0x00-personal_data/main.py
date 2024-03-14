#!/usr/bin/env python3

# Import the get_db function from filtered_logger.py
from filtered_logger import get_db

# Call the get_db function to obtain a database connection
db = get_db()

# Check if the connection was successful
if db:
    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to get the count of users from the 'users' table
    cursor.execute("SELECT COUNT(*) FROM users;")

    # Iterate over the result set and print the count of users
    for row in cursor:
        print(row[0])

    # Close the cursor and database connection
    cursor.close()
    db.close()
