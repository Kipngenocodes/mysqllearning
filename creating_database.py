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

    # Create a cursor object
    cursor = connection.cursor()
    
    # Create a new table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Menu_Descriptions (
        MenuID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(50) NOT NULL,
        Ingredients TEXT,
        Country_of_Origin VARCHAR (200) NOT NULL
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully.")

    # Insert some data into the table
    insert_query = """
    INSERT INTO Menu_Descriptions (Name, Ingredients, Country_of_Origin)
    VALUES (%s, %s, %s)
    """
    data_to_entered= [
            ("Chicken Wings", "Faggio", "Italia"),
            ("Pasta", "Bitter Leaf", "Spain"),
            ("Potato Salad", "Idaho Potatoes", "USA"),
            ("Chicken Salad", "Spinach", "French"),
            ("Fruit Salad", "Orange", "Montana"),
            ("Fries", "Sauce", "Indonesia"),
            ("Chicken Burger", "Burger Mayoinnese ", "Germany"),
            ("Kuku", "Chicken Broth", "Kenya")
            
            ]
    cursor.executemany (insert_query, data_to_entered)
    connection.commit()
    print("Data inserted successfully.")

    # # Execute a SELECT query
    # select_query = "SELECT * FROM Menu"
    # cursor.execute(select_query)
    
    # # Fetch all results
    # results = cursor.fetchall()
    # print("Menu:")
    # for row in results:
    #     print(row)

except connector.Error as err:
    print(f"Error: {err}")

finally:
    if cursor:
        cursor.close()
    if connection.is_connected():
        connection.close()
        print("Connection closed.")
