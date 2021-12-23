from tkinter import *
import sqlite3
from main import *

def show_expresion(gui_vis, expresion):

    result_label = Label(gui_vis, text=expresion)
    result_label.grid(row=0, column=0, columnspan=2)

def show_annually(gui_vis):

    list_all= []

    conn = sqlite3.connect('expenditures.db')
    c = conn.cursor()

    c.execute("SELECT amount FROM expenditures")
    records = c.fetchall()

    for record in records:
        list_all.append(int(record[0]))

    print(list_all)
    expresion = str(sum(list_all))

    conn.commit()
    conn.close()

    show_expresion(gui_vis, expresion)

def show_monthly(gui_vis, month_clicked):

    list_all= []
    choose = month_clicked.get()

    print(choose)

    conn = sqlite3.connect('expenditures.db')
    c = conn.cursor()

    if choose == 'January':
        c.execute("SELECT amount FROM expenditures WHERE month='January'")
    elif choose == 'February':
        c.execute("SELECT amount FROM expenditures WHERE month='February'")
    elif choose == 'March':
        c.execute("SELECT amount FROM expenditures WHERE month='March'")
    elif choose == 'April':
        c.execute("SELECT amount FROM expenditures WHERE month='April'")
    elif choose == 'May':
        c.execute("SELECT amount FROM expenditures WHERE month='May'")
    elif choose == 'June':
        c.execute("SELECT amount FROM expenditures WHERE month='June'")
    elif choose == 'July':
        c.execute("SELECT amount FROM expenditures WHERE month='July'")
    elif choose == 'August':
        c.execute("SELECT amount FROM expenditures WHERE month='August'")
    elif choose == 'September':
        c.execute("SELECT amount FROM expenditures WHERE month='September'")
    elif choose == 'October':
        c.execute("SELECT amount FROM expenditures WHERE month='October'")
    elif choose == 'November':
        c.execute("SELECT amount FROM expenditures WHERE month='November'")
    elif choose == 'December':
        c.execute("SELECT amount FROM expenditures WHERE month='December'")

    records = c.fetchall()

    for record in records:
        list_all.append(int(record[0]))

    print(list_all)
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
    month.config(width=15, padx=5, pady=5)
    month.grid(row=4, column=0)

    Label(gui_vis, text="Expenses throughout the year", font=('Helvetica 9 bold'), bg="lightgray").grid(row=1, column=0, padx=0, pady=0)
    Label(gui_vis, text="Expenses for the whole month", font=('Helvetica 9 bold'), bg="lightgray").grid(row=3, column=0, padx=0, pady=0)

    button_annually = Button(gui_vis, text="Summary annually", bg="gray", height=1, width=20, padx=5, pady=5, command=lambda: show_annually(gui_vis))
    button_monthly = Button(gui_vis, text="Summary monthly", bg="gray", height=1, width=20, padx=5, pady=5, command=lambda: show_monthly(gui_vis, month_clicked))

    button_annually.grid(row=2, column=0)
    button_monthly.grid(row=5, column=0)

def gui_visualisation_settings(gui_vis):

    gui_vis.configure(bg="lightgray")
    gui_vis.title("Visualisation")
    gui_vis.geometry("180x280")

def gui_visualisation_creator(menu):

    gui_vis = Tk()
    gui_visualisation_settings(gui_vis)
    gui_vis_Functionalities(gui_vis)
    menu.destroy()
    gui_vis.mainloop()


