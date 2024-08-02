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

    # Creating a stored procedure
    stored_procedure = """
    CREATE PROCEDURE getCustomer()
    BEGIN
        SELECT menu.Name, menu.Description, menu.Price,
                menu_descriptions.Ingredients, menu_descriptions.Country_of_Origin
        FROM Menu
        INNER JOIN menu_descriptions ON menu.Name = menu_descriptions.Name
        WHERE Price >= 4.99
        ORDER BY Price DESC;
    END
    """
    # Execute the stored procedure creation
    cursor.execute(stored_procedure)
    print('Your stored procedure has been created.')

    # Calling the stored procedure
    cursor.callproc('getCustomer')

    # Fetching the results from the stored procedure call
    results = next(cursor.stored_results())
    my_dataset = results.fetchall()

    # Printing the fetched data
    for data in my_dataset:
        print(data)

except connector.Error as err:
    print(f"Something went wrong: {err}")

finally:
    # Closing the cursor and the connection
    if cursor:
        cursor.close()
        print("Cursor is closed.")
    if connection.is_connected():
        connection.close()
        print("Connection is closed.")
