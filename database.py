from tkinter import *
from main import *
import sqlite3

'''
#CREATE A DATABASE OR CONNECT TO ONE
conn = sqlite3.connect('name.db')

c = conn.cursor()

#CREATE TABLE

c.execute("""CREATE TABLE expenditures(
        id integer,
        month text,
        category text,
        amount integer
        )""")

conn.commit()
conn.close()
'''

def show_records():

    conn = sqlite3.connect('name1.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM expenditures")
    records = c.fetchall()
    print(records)

    conn.commit()
    conn.close()

def submit(amount):

    conn = sqlite3.connect('name1.db')
    c = conn.cursor()

    c.execute("INSERT INTO expenditures VALUES(:amount)",{'amount': amount.get()})

    conn.commit()
    conn.close()

    amount.delete(0, END)

def gui_db_button(gui_db, amount):

    button_submit = Button(gui_db, text="Submit", bg="gray", height=1, width=15, command=lambda:submit(amount))
    button_submit.grid(row=6, column=0, padx=5, pady=2)

def gui_db_dropDownMenu(gui_db):

    month_clicked = StringVar(gui_db)
    month_clicked.set("January")

    month = OptionMenu(gui_db, month_clicked, "January", "February", "March", "April", "May")
    month.grid(row=1, column=0)

    category_clicked = StringVar(gui_db)
    category_clicked.set("Food")

    category = OptionMenu(gui_db, category_clicked, "January", "February", "March", "April", "May")
    category.grid(row=3, column=0)


def gui_db_Label(gui_db):

    Label(gui_db, text="Month", font=('Helvetica 11 bold'), bg="lightgray").grid(row=0, column=0, padx=0, pady=0)
    Label(gui_db, text="Category", font=('Helvetica 11 bold'), bg="lightgray").grid(row=2, column=0, padx=0, pady=0)
    Label(gui_db, text="Amount", font=('Helvetica 11 bold'), bg="lightgray").grid(row=4, column=0, padx=0, pady=0)

'''
def gui_db_Entry(gui_db):

    amount = Entry(gui_db, width=30)
    amount.grid(row=5, column=0, padx=20, pady=5)
'''
def gui_database_creator(gui_db):

    gui_db.configure(bg="lightgray")
    gui_db.title("Add a expenditure")
    gui_db.geometry("230x200")

def database_init():

    gui_db = Tk()
    gui_database_creator(gui_db)
    gui_db_dropDownMenu(gui_db)
    amount = Entry(gui_db, width=30)
    amount.grid(row=5, column=0, padx=20, pady=5)
    #gui_db_Entry(gui_db)
    gui_db_button(gui_db, amount)
    gui_db_Label(gui_db)
    show_records()
    gui_db.mainloop()

