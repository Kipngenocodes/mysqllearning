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
    
    # Filtering the menu
    filtering_menu_data = """
        SELECT Name, Description FROM Menu
        WHERE Name = "Chicken Wings"
        ORDER BY Description DESC
    """
    cursor.execute(filtering_menu_data)
    print("Filtering has been successfully executed as expected!")
    
    # Fetching and printing results
    results = cursor.fetchall()
    for row in results:
        print(f"Name: {row[0]}, Description: {row[1]}")
    print("The process was successfully executed!")
    
except connector.Error as err:
    print(f"Something went wrong: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
        print("Cursor has been closed successfully")
    if connection.is_connected():
        connection.close()
        print("Connection closed successfully")
