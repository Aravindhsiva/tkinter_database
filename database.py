import sqlite3

# ------------------------- Student_Table
# Id | Name | College | Phone | Address

tableName = "student_table"
studentId = "student_id"
studentName = "student_name"
studentCollege = "student_college"
studentPhone = "student_phone"
studentAddress = "student_address"

connection = sqlite3.connect("student.db")
print("Database Working")

# "CREATE TABLE IF NOT EXISTS student_table(student_id "", name "Sanjay", college "Test",....)"
connection.execute(
    "CREATE TABLE IF NOT EXISTS " + tableName + "(" + studentId + " INTEGER PRIMARY KEY AUTOINCREMENT," + studentName +
    " TEXT," + studentCollege + " TEXT, " + studentAddress + " TEXT," + studentPhone + " INTEGER);")
print("Student Added Successfully")


def insert(name, college, address, phone):
    # INSERT INTO
    connection.execute(
        "INSERT INTO " + tableName + " ( " + studentName + ", " + studentCollege + ", " + studentAddress + ", " + studentPhone + " ) VALUES ('" + name + "','" + college + "','" + address + "'," + phone + ")")
    connection.commit()
    return True


def display():
    cursor = connection.execute("SELECT * FROM " + tableName + ";")
    return cursor
