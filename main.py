import tkinter.ttk
from tkinter import *
from tkinter import messagebox

import database as db

root = Tk()

# Requirements
# Simple Student Management Form
# Name, College, Phone, Address => Entry => Db_Add => Db
# Pull Data from DB => show in screen

root = Tk()

root.title("Student Management Form")
root.geometry('600x500')

# Heading
heading = Label(root, text="Student Management Form", font=("Helvetica 12", 20))
heading.grid(row=0, columnspan=2, padx=10, pady=10)

# Form Labels

nameLabel = Label(root, text="Name").grid(row=1, column=0, padx=(10, 20), pady=(30, 20))
collegeLabel = Label(root, text="College").grid(row=2, column=0, padx=(10, 10))
phoneLabel = Label(root, text="Phone No : ").grid(row=3, column=0, padx=10)
addressLabel = Label(root, text="Address").grid(row=4, column=0, padx=10)

nameEntry = Entry(root)
collegeEntry = Entry(root)
phoneEntry = Entry(root)
addressEntry = Entry(root)

nameEntry.grid(row=1, column=1, padx=(0, 10), pady=(30, 20))
collegeEntry.grid(row=2, column=1, padx=(0, 10), pady=20)
phoneEntry.grid(row=3, column=1, padx=(0, 10), pady=20)
addressEntry.grid(row=4, column=1, padx=(0, 10), pady=20)

saveButton = Button(root, text="Save Student", command=lambda: getFormValues())
showButton = Button(root, text="Show Students", command=lambda: showStudents())

saveButton.grid(row=5, column=0)
showButton.grid(row=5, column=1)


# ----------------------------------------------------------------------------------------------

# Functional

def getFormValues():
    name = nameEntry.get()
    college = collegeEntry.get()
    phone = int(phoneEntry.get())
    address = addressEntry.get()

    if db.insert(name, college, address, str(phone)):
        messagebox.showinfo("Saved", "Saved Student Successfully")
    else:
        messagebox.showerror("Error", "Error in saving student")


def showStudents():
    showStudentWin = Tk()
    showStudentWin.title("Students in Database")
    label = Label(showStudentWin, text="Student Management Form")
    label.pack()
    tree = tkinter.ttk.Treeview(showStudentWin)
    tree["columns"] = ("first", "second", "third", "fourth")

    tree.heading("first", text="Name")
    tree.heading("second", text="College")
    tree.heading("third", text="Address")
    tree.heading("fourth", text="Phone")

    dbResult = db.display()

    i = 0
    for student in dbResult:
        tree.insert('', i, text="Student " + str(student[0]), values=(student[1], student[2], student[3], student[4]))
        i = i + 1
    tree.pack()
    showStudentWin.mainloop()


root.mainloop()
