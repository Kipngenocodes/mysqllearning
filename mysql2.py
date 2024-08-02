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
    
    # insertion of data into table 
    mysql_insertion = """ 
        INSERT INTO Menu(Name, Description, Price)
        VALUES(%s, %s, %s)
        
    """
    # Menu Data to be inserted.
    My_Data_Menu =[
        ("Potato Salad", "Delicious Bake", 14.99),
        ("Chicken Salad", "Delicious Bake", 14.99),
        ("Fruit Salad", "Delicious Bake", 14.99),
        ("Chicken Wings", "Delicious Bake", 14.99),
        ("Fries", "Delicious Bake", 4.99),
        ("Chicken Burger", "Delicious Bake", 9.99),
        ("Chicken Pizza", "Delicious Bake", 20.99),
        ("Chicken Wings", "Delicious Bake", 2.99),
        ("Chicken Pizza", "Delicious Peperoni", 4.99),
        ("Chicken Wings", "Delicious Bake", 14.99),
        ("Kuku", "Yum", 2.99)
        
    ]
    
    
    cursor.executemany(mysql_insertion, My_Data_Menu)
    connection.commit()
    print("Data has been inserted as expected. You can manipulate as expected.")
    
except connector.Error as err:
    print("Connection failed!" + err)
    
finally:
    # Closing the cursor and connection
    if cursor:
        cursor.close()
        if connection.is_connected():
            connection.close()
            print("Connection was succesfully! ")
            
