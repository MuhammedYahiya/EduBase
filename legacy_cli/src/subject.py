from db import get_db_connection
from InquirerPy import inquirer

class Subject:
    def __init__(self, subject_name=None, subject_id=None, user_id=None):
        self.subject_name = subject_name
        self.subject_id = subject_id
        self.user_id = user_id
        
    def add_subject(self):
        self.subject_name = inquirer.text(message="Enter subject name:").execute()
        conn = get_db_connection()
        if not conn:
            print("Failed to connect to database")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO subjects (user_id, name) VALUES (%s, %s)",(self.user_id, self.subject_name))
            conn.commit()
            print("Subject added successfully")
            return True
        except Exception as e:
            print(f"Error while adding subject {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def view_subjects(self):
        conn = get_db_connection()
        subject_data = []
        if not conn:
            print("Failed to connect the database")
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name from subjects WHERE user_id = %s", (self.user_id,))
            subjects = cursor.fetchall()
            if not subjects:
                print("No subject found.")
                return []
            for sub in subjects:
                subject_data.append([sub[0],sub[1]])
        except Exception as e:
            print("Error retrieving subjects: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
        
        return subject_data
        
    def search_subject(self):
        conn = get_db_connection()
        if not conn:
            print("Failed to connect the database")
            return []
        sub_name = inquirer.text("Please enter the subject name for search:").execute()
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name FROM subjects WHERE user_id=%s",(self.user_id,))
            subjects = cursor.fetchall()
            if not subjects:
                print("No Subject Found")
                return []
            
            matched_subjects = []
            
            for sub in subjects:
                if sub_name.lower() in sub[1].lower():
                    matched_subjects.append(sub[1])
                    
            return matched_subjects
    
        except Exception as e:
            print("Error searching subjects: {e}")
        finally:
            cursor.close()
            conn.close()
            
    def sort_subject(self, choice=None):
        conn = get_db_connection()
        if not conn:
            print("Failed to connect the db")
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM subjects WHERE user_id = %s",(self.user_id,))
            subjects = [sub[0] for sub in cursor.fetchall()]
            if not subjects:
                print("No subjects found")
                return[]
            
            if choice == 'A-Z':
                subjects.sort(key=lambda x: x.lower())
                return subjects
            elif choice == 'Z-A':
                subjects.sort(reverse=True, key=lambda x: x.lower())
                return subjects
            
        except Exception as e:
            print(f"Error while sorting subjects: {e}")
            return[]
        finally:
            cursor.close()
            conn.close()
            