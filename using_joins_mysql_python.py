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
    
    # Joining of data into table 
    mysql_join = """ 
        SELECT Menu.Name, Menu.Description, Menu.Price FROM Menu
        OUTER JOIN Menu_Descriptions ON Menu.Name = Menu_Descriptions.Name
        Order by Name Desc
        
    """
    
    
    
    cursor.execute(mysql_join)
    result = cursor.fetchall()
    print("Data has been Joined as expected. You can now enjoy as expected.")
    
    for x in result:
        print(x)
    
except connector.Error as err:
    print("Connection failed!" + err)
    
finally:
    # Closing the cursor and connection
    if cursor:
        cursor.close()
        if connection.is_connected():
            connection.close()
            print("Connection was succesfully! ")
            
