from db import get_db_connection
from InquirerPy import inquirer

def add_subject(user_id):
    subject_name = inquirer.text(message="Enter subject name:").execute()
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO subjects (user_id, name) VALUES (%s, %s)",(user_id, subject_name))
        conn.commit()
        cursor.close()
        conn.close()
        print("Subject added successfully.")
    else:
        print("Failed to connect to database.")