import mysql.connector as connector

try:
    # Creating a connection to the database
    connection = connector.connect(
        host='localhost',
        user='root',
        password='Kapsabet',
        database='LittleLemonDB'
    )
    print("Connection has been established.")

    # Creating a cursor object
    cursor = connection.cursor()

    # Calling the stored procedure
    cursor.callproc('getCustomer')

    # Printing the results
    for result in cursor.stored_results():
        print(result.fetchall())  # Fetch and print all results returned by the stored procedure

except connector.Error as err:
    print(f"Something went wrong: {err}")

finally:
    # Ensure that the cursor and connection are closed to avoid memory leaks
    if cursor:
        cursor.close()
        print("Cursor is closed")
    if connection:
        connection.close()
        print("Connection is closed")
