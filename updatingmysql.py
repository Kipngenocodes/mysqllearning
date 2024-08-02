import mysql.connector as connector

try:
    # Establish the connection
    connection = connector.connect(
        host="localhost",
        user="root",       # Replace with your MySQL username
        password="Kapsabet",   # Replace with your MySQL password
        database="LittleLemonDB"  # Replace with your database name
    )
    
    if connection.is_connected():
        print("Connection established!")

    # Creating a cursor connection
    cursor = connection.cursor()
    
    # SQL Query to increment each date by 4 days
    update_query = """
        UPDATE Menu
        SET Hire_date = DATE_ADD(Hire_date, INTERVAL 4 DAY);
    """
    
    cursor.execute(update_query)
    connection.commit()  # Commit the change
    print("All dates have been incremented by four days successfully.")

except connector.Error as err:
    print("Connection failed: " + str(err))
    
finally:
    # Closing the cursor and connection
    if cursor:
        cursor.close()
        print("Cursor closed.")
    if connection.is_connected():
        connection.close()
        print("Connection closed successfully.")
