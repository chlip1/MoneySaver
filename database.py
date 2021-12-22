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
def gui_db_dropDownMenu(gui_db):

    clicked = StringVar(gui_db)
    clicked.set("January")

    drop = OptionMenu(gui_db, clicked, "January", "February", "March", "April", "May")
    drop.grid(row=1, column=0)

def gui_db_Label(gui_db):
    Label(gui_db, text="Month", font=('Helvetica 11 bold'), bg="lightgray").grid(row=0, column=0, padx=0, pady=0)
    Label(gui_db, text="Category", font=('Helvetica 11 bold'), bg="lightgray").grid(row=2, column=0, padx=0, pady=0)
    Label(gui_db, text="Amount", font=('Helvetica 11 bold'), bg="lightgray").grid(row=4, column=0, padx=0, pady=0)

def gui_db_Entry(gui_db):

    category = Entry(gui_db, width=30)
    category.grid(row=3, column=0, padx=20, pady=5)

    amount = Entry(gui_db, width=30)
    amount.grid(row=5, column=0, padx=20, pady=5)

def gui_database_creator(gui_db):

    gui_db.configure(bg="lightgray")
    gui_db.title("Add a expenditure")
    gui_db.geometry("230x240")

def database_init():

    gui_db = Tk()
    gui_database_creator(gui_db)
    gui_db_dropDownMenu(gui_db)
    gui_db_Entry(gui_db)
    gui_db_Label(gui_db)
    gui_db.mainloop()
