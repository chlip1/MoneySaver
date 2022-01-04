from tkinter import *
import sqlite3
import database
from main import *
from database import *
from matplotlib import pyplot as plt

def create_list_per_category(dev_y):

    list_all = []
    dev_y.clear()
    conn = sqlite3.connect('expenditures.db')
    c = conn.cursor()

    categories = [("Grocery shopping",), ("Food from restaurant",), ("Car fuel",),
                  ("Car extra expenses",), ("Investments",), ("Gifts and loan",), ("Clothes",), ("House",), ("Subscription",), ("Extra",)]

    for category in categories:
        c.execute("SELECT amount FROM expenditures WHERE category=?", category)

        records = c.fetchall()

        for record in records:
            list_all.append(int(record[0]))

        expresion = str(sum(list_all))
        dev_y.append(expresion)
        list_all.clear()

    conn.commit()
    conn.close()

    for i in range(0, len(dev_y)):
        dev_y[i] = int(dev_y[i])

    print(dev_y)
    return dev_y

def create_list_per_month(dev_y):

    list_all=[]
    dev_y.clear()
    conn = sqlite3.connect('expenditures.db')
    c = conn.cursor()

    months = [("January",), ("February",), ("March",), ("April",), ("May",),
    ("June",), ("July",), ("August",), ("September",), ("October",), ("November",), ("December",)]

    for month in months:
        c.execute("SELECT amount FROM expenditures WHERE month=?",month)

        records = c.fetchall()

        for record in records:
            list_all.append(int(record[0]))

        expresion = str(sum(list_all))
        dev_y.append(expresion)
        list_all.clear()

    conn.commit()
    conn.close()

    for i in range(0, len(dev_y)):
        dev_y[i] = int(dev_y[i])

    return dev_y

def show_monthly_bar():

    dev_x = ["Jan", "Feb", "Mar", "Apr", "May",
             "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
    dev_y=[]

    create_list_per_month(dev_y)

    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.title("Expenditures per month")

    plt.bar(dev_x, dev_y)
    plt.show()

def show_category_bar():

    dev_x = ["Grocery", "Dinner", "Car fuel",
    "Car extra", "Investments", "Gifts", "Clothes", "House", "Subscription", "Extra"]

    dev_y = []

    create_list_per_category(dev_y)
    plt.figure(figsize=(12, 6))

    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title("Expenditures per category")


    plt.bar(dev_x, dev_y)
    plt.show()

def show_expresion(gui_vis, expresion):

    result_label = Label(gui_vis, text=expresion)
    result_label.grid(row=0, column=0, columnspan=2)

def category_per_month(gui_vis, category_clicked):
    list_all = []

    choose = ("{}".format(category_clicked.get()),)
    conn = sqlite3.connect('expenditures.db')
    c = conn.cursor()

    c.execute("SELECT amount FROM expenditures WHERE category=?", choose)

    records = c.fetchall()

    for record in records:
        list_all.append(int(record[0]))

    expresion = str(sum(list_all))

    conn.commit()
    conn.close()

    show_expresion(gui_vis, expresion)

def show_annually(gui_vis):

    list_all= []

    conn = sqlite3.connect('expenditures.db')
    c = conn.cursor()

    c.execute("SELECT amount FROM expenditures")
    records = c.fetchall()

    for record in records:
        list_all.append(int(record[0]))

    expresion = str(sum(list_all))

    conn.commit()
    conn.close()

    show_expresion(gui_vis, expresion)

def show_monthly(gui_vis, month_clicked):

    list_all= []

    choose = ("{}".format(month_clicked.get()),)
    conn = sqlite3.connect('expenditures.db')
    c = conn.cursor()

    c.execute("SELECT amount FROM expenditures WHERE month=?",choose)

    records = c.fetchall()

    for record in records:
        list_all.append(int(record[0]))

    expresion = str(sum(list_all))

    conn.commit()
    conn.close()

    show_expresion(gui_vis, expresion)

def gui_vis_Functionalities(gui_vis):

    expresion = ":)"
    show_expresion(gui_vis, expresion)

    month_clicked = StringVar(gui_vis)
    month_clicked.set("January")

    month = OptionMenu(gui_vis, month_clicked, "January", "February", "March", "April", "May",
                       "June", "July", "August", "September", "October", "November", "December")
    month.config(width=20, padx=5, pady=5)
    month.grid(row=4, column=0)

    category_clicked = StringVar(gui_vis)
    category_clicked.set("Grocery shopping")

    category = OptionMenu(gui_vis, category_clicked, "Grocery shopping", "Food from restaurant", "Car fuel",
                          "Car extra expenses", "Investments", "Gifts and loan", "Clothes", "House", "Subscription", "Extra")
    category.config(width=20, padx=5, pady=5)
    category.grid(row=7, column=0)

    Label(gui_vis, text="Expenses throughout the year", font=('Helvetica 9 bold'), bg="lightgray").grid(row=1, column=0, padx=0, pady=0)
    Label(gui_vis, text="Expenses for the whole month", font=('Helvetica 9 bold'), bg="lightgray").grid(row=3, column=0, padx=0, pady=0)
    Label(gui_vis, text="Expenses per category", font=('Helvetica 9 bold'), bg="lightgray").grid(row=6, column=0, padx=0, pady=0)
    Label(gui_vis, text="Show plots", font=('Helvetica 9 bold'), bg="lightgray").grid(row=9, column=0, padx=0, pady=0)

    button_annually = Button(gui_vis, text="Summary annually", bg="gray", height=1, width=25, padx=5, pady=5, command=lambda: show_annually(gui_vis))
    button_monthly = Button(gui_vis, text="Summary monthly", bg="gray", height=1, width=25, padx=5, pady=5, command=lambda: show_monthly(gui_vis, month_clicked))
    button_per_category = Button(gui_vis, text="Summary per category", bg="gray", height=1, width=25, padx=5, pady=5, command=lambda: category_per_month(gui_vis, category_clicked))
    button_plot_month = Button(gui_vis, text="Month bar", bg="gray", height=1, width=12, padx=5, pady=5, command=show_monthly_bar)
    button_plot_category = Button(gui_vis, text="Category bar", bg="gray", height=1, width=12, padx=5, pady=5, command=show_category_bar)

    button_exit = Button(gui_vis, text="Back", bg="gray", height=1, width=25,
                         command=lambda: database.db_close(gui_vis))

    button_annually.grid(row=2, column=0)
    button_monthly.grid(row=5, column=0)
    button_per_category.grid(row=8, column=0)
    button_plot_month.grid(row=10, column=0)
    button_plot_category.grid(row=11, column=0)
    button_exit.grid(row=12, column=0, padx=5, pady=2)

def gui_visualisation_settings(gui_vis):

    gui_vis.configure(bg="lightgray")
    gui_vis.title("Visualisation")
    gui_vis.geometry("195x400")

def gui_visualisation_creator(menu):

    gui_vis = Tk()
    gui_visualisation_settings(gui_vis)
    gui_vis_Functionalities(gui_vis)
    menu.destroy()
    gui_vis.mainloop()


