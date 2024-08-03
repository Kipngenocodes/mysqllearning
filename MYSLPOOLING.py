import mysql.connector
from mysql.connector import Error
from mysql.connector.pooling import MySQLConnectionPool

try:
    # Create a connection pool named 'LittleLemonPool'
    pool = MySQLConnectionPool(
        pool_name="LittleLemonPool",
        pool_size=5,
        pool_reset_session=True,
        host='localhost',
        user='root',
        password='Kapsabet',
        database='LittleLemonDB'
    )
    print("Connection pool is created successfully.")

    # Get connection from connection pool
    connection = pool.get_connection()

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL database using connection pool... MySQL Server version on ", db_Info)

        # Create a cursor object using the connection
        cursor = connection.cursor()
        cursor.execute("select database();")   
        record = cursor.fetchone()
        print("You're connected to - ", record)
# Handling of errors.
except Error as e:
    print("Error while connecting to MySQL using Connection pool ", e)

finally:
    # Closing the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

