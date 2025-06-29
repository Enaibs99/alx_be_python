import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='OgheneTejiri99'   # Replace this with the actual password
    )

    if connection.is_connected():
        print("✅ Connected to MySQL Server successfully!")

except Error as e:
    print(f"❌ Connection error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()