from db import get_db_connection
from InquirerPy import inquirer

def register_user():
    username = inquirer.text(message="Enter your username:").execute()
    password = inquirer.text(message="Enter your password:").execute()
    
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)",(username, password))
        conn.commit()
        cursor.close()
        conn.close()
        print("Registration successful!")
        return True
    else:
        print("Database connection failed")
        return False
        
        
def login_user():
    username = inquirer.text(message="Enter your username:").execute()
    password = inquirer.text(message="Enter your password:").execute()
    
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s",(username, password))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            print("Login successful!")
            return True
        else:
            print("Invalid credentials.")
            return False
    else:
        print("Database connection failed")
        return False




