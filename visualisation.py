from tkinter import *
import sqlite3
import database
import plots
import main

def show_expresion(gui_vis, expresion):
    #SHOW RESULT OF EXPRESION
    result_label = Label(gui_vis, text=expresion)
    result_label.grid(row=0, column=0, columnspan=2)

def db_close(gui_vis):

    gui_vis.destroy()
    main.menu_init()

def show_category_expenses(gui_vis, category_clicked):
    #CHOOSE EXPENSES FOR EACH MONTH FROM DATABASE AND SUM THEM
    list_all = []

    choose = ("{}".format(category_clicked.get()),)
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()

    c.execute("SELECT amount FROM expenses WHERE category=?", choose)

    records = c.fetchall()

    for record in records:
        list_all.append(int(record[0]))

    expresion = str(sum(list_all))

    conn.commit()
    conn.close()

    show_expresion(gui_vis, expresion)

def show_annually_expenses(gui_vis):

    list_all= []

    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()

    c.execute("SELECT amount FROM expenses")
    records = c.fetchall()

    for record in records:
        list_all.append(int(record[0]))

    expresion = str(sum(list_all))

    conn.commit()
    conn.close()

    show_expresion(gui_vis, expresion)

def show_monthly_expenses(gui_vis, month_clicked):

    list_all= []

    choose = ("{}".format(month_clicked.get()),)
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()

    c.execute("SELECT amount FROM expenses WHERE month=?",choose)

    records = c.fetchall()

    for record in records:
        list_all.append(int(record[0]))

    expresion = str(sum(list_all))

    conn.commit()
    conn.close()

    show_expresion(gui_vis, expresion)

def gui_vis_Functionalities(gui_vis):
    #ALL NEEDED FUNCTIONALITIES
    expresion = ":)"
    show_expresion(gui_vis, expresion)
    #OPTIONS MENUS
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
    #LABELS
    Label(gui_vis, text="Expenses throughout the year", font=('Helvetica 9 bold'), bg="lightgray").grid(row=1, column=0, padx=0, pady=0)
    Label(gui_vis, text="Expenses for the whole month", font=('Helvetica 9 bold'), bg="lightgray").grid(row=3, column=0, padx=0, pady=0)
    Label(gui_vis, text="Expenses per category", font=('Helvetica 9 bold'), bg="lightgray").grid(row=6, column=0, padx=0, pady=0)
    Label(gui_vis, text="Show plots", font=('Helvetica 9 bold'), bg="lightgray").grid(row=9, column=0, padx=0, pady=0)
    #BUTTONS
    button_annually = Button(gui_vis, text="Summary annually", bg="gray", height=1, width=25, padx=5, pady=5, command=lambda: show_annually_expenses(gui_vis))
    button_monthly = Button(gui_vis, text="Summary monthly", bg="gray", height=1, width=25, padx=5, pady=5, command=lambda: show_monthly_expenses(gui_vis, month_clicked))
    button_per_category = Button(gui_vis, text="Summary per category", bg="gray", height=1, width=25, padx=5, pady=5, command=lambda: show_category_expenses(gui_vis, category_clicked))
    button_plot_month = Button(gui_vis, text="Month bar", bg="gray", height=1, width=12, padx=5, pady=5, comman=lambda: plots.show_monthly_bar())
    button_plot_category = Button(gui_vis, text="Category bar", bg="gray", height=1, width=12, padx=5, pady=5, command=lambda: plots.show_category_bar())

    button_exit = Button(gui_vis, text="Back", bg="gray", height=1, width=25,
                         command=lambda: db_close(gui_vis))
    #SHOW BUTTONS
    button_annually.grid(row=2, column=0)
    button_monthly.grid(row=5, column=0)
    button_per_category.grid(row=8, column=0)
    button_plot_month.grid(row=10, column=0)
    button_plot_category.grid(row=11, column=0)
    button_exit.grid(row=12, column=0, padx=5, pady=2)

def gui_visualisation_settings(gui_vis):
    #SIMPLE CONFIG OF GUI
    gui_vis.configure(bg="lightgray")
    gui_vis.title("Visualisation")
    gui_vis.geometry("195x400")

def gui_visualisation_creator(menu):
    # TRY TO INIT DATABASE
    database.init_database()
    # INIT SIMPLE GUI
    gui_vis = Tk()
    gui_visualisation_settings(gui_vis)
    # SHOW LABELS, BUTTONS ETC
    gui_vis_Functionalities(gui_vis)
    # DESTROY PREVIOUS GUI
    menu.destroy()
    #START GUI
    gui_vis.mainloop()


