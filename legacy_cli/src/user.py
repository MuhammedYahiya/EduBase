from db import get_db_connection
from InquirerPy import inquirer
import bcrypt

class User:
    def __init__(self, username=None, user_id=None):
        self.username = username
        self.user_id = user_id
        
    def register(self):
        self.username = inquirer.text(message="Enter your username:").execute()
        password = inquirer.text(message="Enter your password:").execute()
        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        
        conn = get_db_connection()
        if not conn:
            print("Database connection failed")
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUE (%s, %s)",(self.username, hash_password))
            conn.commit()
            print("Registration successful!")
            return True
        except Exception as e:
            print(f"Error during registration: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def login(self):
        self.username = inquirer.text(message="Enter your username:").execute()
        password = inquirer.text(message="Enter your password").execute()
        
        conn = get_db_connection()
        if not conn:
            print("Database connection failed")
            return False
            
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, password FROM users WHERE username=%s",(self.username,))
            result = cursor.fetchall()
            if not result:
                print("No user found with that username.")
                
            user_id, hashed_password = result[0]
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                self.user_id = user_id
                print("Login successful!")
                return True
            else:
                print("Invalid credentials.")
                return False
        except Exception as e:
            print(f"Login error: {e}")
            return False
        finally:
            cursor.close()
            conn.close()