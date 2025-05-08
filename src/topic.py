from db import get_db_connection
from InquirerPy import inquirer

class Topic:
    def __init__(self, subject_id=None, topic_name=None, topic_id=None, completed=False):
        self.subject_id = subject_id
        self.topic_name = topic_name
        self.topic_id = topic_id
        self.completed = completed
        
    def add_topic(self):
        self.topic_name = inquirer.text(message="Enter topic name:").execute()
        
        conn = get_db_connection()
        if not conn:
            print("Failed to connect to the database")
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO topics (subject_id, name, completed) VALUES (%s, %s, %s)",(self.subject_id, self.topic_name, self.completed))
            conn.commit()
            print("Topic added successfully")
            return True
        except Exception as e:
            print(f"Error while adding topic {e}")
            return False
        finally:
            cursor.close()
            conn.close()
            
    def view_topics(self):
        conn = get_db_connection()
        topic_data = []
        
        if not conn:
            print("Failed to connect the database")
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, completed FROM topics WHERE subject_id=%s",(self.subject_id,))
            result = cursor.fetchall()
            
            for topic in result:
                topic_data.append([topic[0], topic[1], topic[2]])
                
        except Exception as e:
            print(f"Error while fetching topics {e}")
        finally:
            cursor.close()
            conn.close()
        
        return topic_data

    def marked_as_completed(self):
        conn = get_db_connection()
        if not conn:
            print("Failed to connect the database")
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE topics SET completed=%s WHERE id=%s",(True, self.topic_id))
            conn.commit()
            print("Topic marked as completed successfully.")
            return True
        except Exception as e:
            print(f"Failed to update the topic {e}")
            return False
        finally:
            cursor.close()
            conn.close()
        
