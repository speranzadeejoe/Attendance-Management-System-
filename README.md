# Attendance-Management-System-
## **📌 Attendance Management System**  
A simple **Tkinter-based Attendance Management System** integrated with **MySQL** to add students, mark attendance, and view attendance records.  

---

## **🛠 Features**  
✔ **Add Students** – Store student names in the database.  
✔ **Mark Attendance** – Select a student and mark their attendance as **Present, Absent, or Late**.  
✔ **View Attendance** – Display attendance records in a tabular format.  
✔ **Database Integration** – Uses **MySQL** to store student and attendance data.  
✔ **User-Friendly GUI** – Built with **Tkinter** for an interactive experience.  

---

## **💂️ Project Structure**  
```
📆 Attendance-Management-System
 ├ 💜 main.py         # GUI for the system (Tkinter)
 ├ 💜 db.py           # Database connection & operations (MySQL)
 ├ 💜 attendance_management.sql  # SQL file for database setup
 ├ 💜 README.md       # Project documentation
 └ 💜 requirements.txt # Required Python libraries
```

---

## **🚀 Setup & Installation**  

### **1⃣ Install Required Libraries**  
Run the following command:  
```sh
pip install mysql-connector-python tk
```

### **2⃣ Set Up MySQL Database**  
- Open MySQL and create the database using the provided SQL file:
  ```sh
  mysql -u root -p < attendance_management.sql
  ```
- Update **MySQL credentials** in `db.py`:  
  ```python
  conn = mysql.connector.connect(
      host="localhost",
      user="root",  # Change if needed
      password="mini",  # Update your MySQL password
      database="attendance_management",
      port=3306
  )
  ```

### **3⃣ Run the Project**  
- **Run `db.py` once** to create the tables:  
  ```sh
  python db.py
  ```
- Then, start the GUI:  
  ```sh
  python main.py
  ```

---

## **🖥️ Usage Guide**  
1⃣ **Add Student** → Enter a name and click **"Add Student"**  
2⃣ **Mark Attendance** → Select a student, choose status, and click **"Mark Attendance"**  
3⃣ **View Attendance** → Attendance records appear in the table  

---

## **🛠 Tech Stack**  
- **Python** (Tkinter for GUI)  
- **MySQL** (Database Management)  

---

## **💡 Future Enhancements**  
- 📌 Export attendance records to Excel/CSV  
- 📌 Search & filter attendance records  
- 📌 User authentication system  

---

## **📞 Support & Contribution**  
If you have any suggestions or find any issues, feel free to **raise an issue** or **contribute**! 🚀  

---

