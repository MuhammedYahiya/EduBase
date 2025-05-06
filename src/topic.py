from db import get_db_connection
from InquirerPy import inquirer

def add_topic(subject_id):
    topic_name = inquirer.text(message="Enter topic name:").execute()
    conn = get_db_connection()
    if not conn:
        print("Failed to Connect to the database")
        return None
    
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO topics (subject_id, name, completed) VALUES  (%s, %s, %s)",(subject_id, topic_name, False))
        conn.commit()
        print("Topic added successfully.")
    except Exception as e:
        print(f"Error while adding the  topics: {e}")
        
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        

        
