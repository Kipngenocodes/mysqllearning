import mysql.connector as connector

try:
    # Establish the connection
    connection = connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="Kapsabet",  # Replace with your MySQL password
        database="LittleLemonDB"  # Replace with your database name
    )
    
    if connection.is_connected():
        print("Connection established!")

    # Creating a cursor connection
    cursor = connection.cursor()
    
    # Altering the data in the table by adding a new column
    data_altering = """
        ALTER TABLE Menu
        DROP COLUMN date;
    """
    
    cursor.execute(data_altering)
    connection.commit()  # Commit the changes to apply the ALTER TABLE
    print("Table altered successfully. 'date' column added to 'Menu'.")
    
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
