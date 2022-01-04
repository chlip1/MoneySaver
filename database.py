from tkinter import *
import main
import sqlite3

def init_database():

    try:
        #CREATE A DATABASE OR CONNECT TO ONE
        conn = sqlite3.connect('expenses.db')
        c = conn.cursor()

        #CREATE TABLE
        c.execute("""CREATE TABLE expenses(
                amount integer,
                month text,
                category text,
                descriptions text
                )""")

        conn.commit()
        conn.close()

    except:
        #IF DATABASE EXISTS RETURN
        return

def db_close(gui_db):

    gui_db.destroy()
    main.menu_init()

def submit(amount, month_clicked, category_clicked, descriptions):
    #ADDING A VARIABLE TO THE DATABASE
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()

    c.execute("INSERT INTO expenses VALUES(:amount, :month, :category, :descriptions)",{'amount': amount.get(),
                                                                  'month': month_clicked.get(),
                                                                  'category':category_clicked.get(),
                                                                  'descriptions': descriptions.get()})

    conn.commit()
    conn.close()

    #RESET ENTRY
    amount.delete(0, END)
    descriptions.delete(0, END)

def gui_Functionalities(gui_db):
    #LABELS
    Label(gui_db, text="Month", font=('Helvetica 11 bold'), bg="lightgray").grid(row=0, column=0, padx=0, pady=0)
    Label(gui_db, text="Category", font=('Helvetica 11 bold'), bg="lightgray").grid(row=2, column=0, padx=0, pady=0)
    Label(gui_db, text="Amount", font=('Helvetica 11 bold'), bg="lightgray").grid(row=4, column=0, padx=0, pady=0)
    Label(gui_db, text="Descriptions", font=('Helvetica 11 bold'), bg="lightgray").grid(row=6, column=0, padx=0, pady=0)
    #OPTION MENUS
    month_clicked = StringVar(gui_db)
    month_clicked.set("January")

    month = OptionMenu(gui_db, month_clicked, "January", "February", "March", "April", "May",
                       "June", "July", "August", "September", "October", "November", "December")
    month.grid(row=1, column=0)

    category_clicked = StringVar(gui_db)
    category_clicked.set("Food from restaurant")

    category = OptionMenu(gui_db, category_clicked, "Grocery shopping", "Food from restaurant", "Car fuel",
                          "Car extra expenses", "Investments", "Gifts and loan", "Clothes", "House", "Subscription", "Extra")
    category.grid(row=3, column=0)
    #ENTRY VARIABLES
    amount = Entry(gui_db, width=30)
    amount.grid(row=5, column=0, padx=20, pady=5)

    descriptions = Entry(gui_db, width=30)
    descriptions.grid(row=7, column=0, padx=20, pady=5)
    #SHOW BUTTONS
    button_submit = Button(gui_db, text="Submit", bg="gray", height=1, width=15,
                           command=lambda: submit(amount, month_clicked, category_clicked, descriptions))
    button_submit.grid(row=8, column=0, padx=5, pady=2)

    button_exit = Button(gui_db, text="Back", bg="gray", height=1, width=15,
                           command=lambda: db_close(gui_db))
    button_exit.grid(row=9, column=0, padx=5, pady=2)

def gui_database_settings(gui_db):
    #SIMPLE CONFIG OF GUI
    gui_db.configure(bg="lightgray")
    gui_db.title("Add a expense")
    gui_db.geometry("230x280")

def gui_database_creator(menu):
    #TRY TO INIT DATABASE
    init_database()
    # INIT SIMPLE GUI
    gui_db = Tk()
    gui_database_settings(gui_db)
    #SHOW LABELS, BUTTONS ETC
    gui_Functionalities(gui_db)
    # DESTROY PREVIOUS GUI
    menu.destroy()
    #START GUI
    gui_db.mainloop()

