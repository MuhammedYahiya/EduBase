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
        

def view_subjects(user_id):
    conn = get_db_connection()
    subject_data = []
    if not conn:
        print("Failed to Connect to the database")
        return None
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * from subjects where user_id = %s", (user_id,))
        subjects = cursor.fetchall()
        for subject in subjects:
            subject_data.append((subject[0], subject[2]))
    except Exception as e:
        print(f"Error retrieving subjects: {e}")
    finally:
        cursor.close()
        conn.close()
        
    return subject_data
    
    