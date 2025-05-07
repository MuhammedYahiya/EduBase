from db import get_db_connection
import csv
import os

def export_progress(user_id):
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to the database.")
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT s.name AS subject_name, t.name AS topic_name, t.completed 
                       FROM subjects s 
                       JOIN topics t ON s.id = t.subject_id
                       WHERE s.user_id = %s
                       """, (user_id,))
        records = cursor.fetchall()
        
        if not records:
            print("No progress data to export")
            return
        
        backup_dir = "Reports"
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        filename = os.path.join(backup_dir, f"user_{user_id}_progress.csv")
        
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Subject", "Topic","Completed"])
            
            for subject_name, topic_name, completed in records:
                writer.writerow([subject_name, topic_name, bool(completed)])
                
        print(f"Progress exported successfully to {filename}")
    except Exception as e:
        print(f"Error exporting progress: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()