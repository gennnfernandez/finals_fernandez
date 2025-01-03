import sqlite3

DB_NAME = "ict_training.db"

def initialize_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            duration TEXT NOT NULL,
            trainer TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_course(title, description, duration, trainer):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (title, description, duration, trainer) VALUES (?, ?, ?, ?)", 
                   (title, description, duration, trainer))
    conn.commit()
    conn.close()

def read_courses():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    records = cursor.fetchall()
    conn.close()
    return records

def update_course(course_id, title, description, duration, trainer):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE courses SET title = ?, description = ?, duration = ?, trainer = ? WHERE id = ?", 
                   (title, description, duration, trainer, course_id))
    conn.commit()
    conn.close()

def delete_course(course_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
    conn.commit()
    conn.close()
