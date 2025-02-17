import tkinter as tk
from tkinter import ttk, messagebox
import db  # Import database functions from db.py

# 🔹 Function to Add Student
def add_student():
    name = entry_name.get()
    if db.add_student(name):
        messagebox.showinfo("Success", "Student added successfully!")
        entry_name.delete(0, tk.END)
        load_students()
    else:
        messagebox.showerror("Error", "Failed to add student.")

# 🔹 Function to Load Students into Listbox
def load_students():
    student_listbox.delete(0, tk.END)
    students = db.fetch_students()
    for student in students:
        student_listbox.insert(tk.END, f"{student[0]} - {student[1]}")

# 🔹 Function to Mark Attendance
def mark_attendance():
    selected = student_listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a student.")
        return

    student_id = student_listbox.get(selected[0]).split(" - ")[0]
    status = attendance_status.get()

    if db.mark_attendance(student_id, status):
        messagebox.showinfo("Success", "Attendance marked successfully!")
        load_attendance()
    else:
        messagebox.showerror("Error", "Failed to mark attendance.")

# 🔹 Function to Load Attendance Data
def load_attendance():
    for row in tree.get_children():
        tree.delete(row)

    records = db.fetch_attendance()
    for record in records:
        tree.insert("", tk.END, values=record)

# 🔹 GUI Setup
root = tk.Tk()
root.title("Attendance Management System")
root.geometry("600x500")

# 🔹 Title Label
title_label = tk.Label(root, text="Attendance Management System", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# 🔹 Student Entry Frame
student_frame = tk.Frame(root)
student_frame.pack(pady=5)
tk.Label(student_frame, text="Student Name:").grid(row=0, column=0, padx=5)
entry_name = tk.Entry(student_frame, width=20)
entry_name.grid(row=0, column=1, padx=5)
btn_add = tk.Button(student_frame, text="Add Student", command=add_student)
btn_add.grid(row=0, column=2, padx=5)

# 🔹 Student Listbox
student_listbox = tk.Listbox(root, height=5)
student_listbox.pack(pady=5, fill=tk.X, padx=20)

# 🔹 Attendance Section
attendance_frame = tk.Frame(root)
attendance_frame.pack(pady=5)
tk.Label(attendance_frame, text="Status:").grid(row=0, column=0, padx=5)
attendance_status = ttk.Combobox(attendance_frame, values=["Present", "Absent", "Late"], state="readonly")
attendance_status.grid(row=0, column=1, padx=5)
attendance_status.current(0)
btn_mark = tk.Button(attendance_frame, text="Mark Attendance", command=mark_attendance)
btn_mark.grid(row=0, column=2, padx=5)

# 🔹 Attendance Table (Treeview)
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10)

columns = ("ID", "Name", "Date", "Status")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack()

# 🔹 Load Data at Startup
load_students()
load_attendance()

# Run Application
root.mainloop()
