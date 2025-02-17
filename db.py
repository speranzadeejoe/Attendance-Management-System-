import mysql.connector
from tkinter import messagebox
from datetime import date

# 🔹 Connect to MySQL Database
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mini",
            database="attendance_management",
            port=3306
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

# 🔹 Create Tables (Run this once)
def create_tables():
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    
    # Create Students Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
    """)

    # Create Attendance Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT NOT NULL,
            date DATE NOT NULL,
            status ENUM('Present', 'Absent', 'Late') NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
        )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()

# 🔹 Add a Student to the Database
def add_student(name):
    if not name:
        messagebox.showwarning("Input Error", "Please enter a student name.")
        return False
    
    conn = connect_db()
    if conn is None:
        return False
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO students (name) VALUES (%s)", (name,))
        conn.commit()
        return True
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return False
    finally:
        cursor.close()
        conn.close()

# 🔹 Fetch All Students
def fetch_students():
    conn = connect_db()
    if conn is None:
        return []
    
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM students")
    students = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return students

# 🔹 Mark Attendance
def mark_attendance(student_id, status):
    conn = connect_db()
    if conn is None:
        return False
    
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (%s, %s, %s)", 
                       (student_id, date.today(), status))
        conn.commit()
        return True
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return False
    finally:
        cursor.close()
        conn.close()

# 🔹 Fetch Attendance Records
def fetch_attendance():
    conn = connect_db()
    if conn is None:
        return []
    
    cursor = conn.cursor()
    cursor.execute("""
        SELECT students.id, students.name, attendance.date, attendance.status 
        FROM students 
        JOIN attendance ON students.id = attendance.student_id
    """)
    records = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return records

# Run Table Creation (Only Once)
create_tables()
