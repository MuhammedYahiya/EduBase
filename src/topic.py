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
            
def view_topics(subject_id):
    conn = get_db_connection()
    topic_data = []
    if not conn:
        print("Failed to connect to the database")
        return None
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, completed FROM topics WHERE  subject_id=%s ",(subject_id,))
        topics = cursor.fetchall()
        for topic in topics:
            topic_data.append((topic[0], topic[1], topic[2]))
    except Exception as e:
        print(f"Error while fetching the topics: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return topic_data
        
def mark_as_completed(topic_id):
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to the database")
        return None
    
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE topics SET completed= %s WHERE id = %s",(True, topic_id))
        conn.commit()
        print("Topic marked as successfully.")
    except Exception as e:
        print(f"Error while updating the topics: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()