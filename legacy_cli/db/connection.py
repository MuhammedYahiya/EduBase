from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error

load_dotenv()



def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if connection.is_connected():
            return connection
        
    except Error as e:
        print(f"[DB Error] {e}")
        return None