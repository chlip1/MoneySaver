from tkinter import *

def menu_settings(menu):
    # SETTINGS
    menu.configure(bg="deep sky blue")
    menu.title("MENU")
    menu.geometry("230x240")

def menu_buttons(menu):
    # INIT BUTTONS
    button_database = Button(menu, text="Add a expenditure", bg="gray", height=3, width=30)
    button_visualisation = Button(menu, text="Show past expenditures", bg="gray", height=3, width=30)
    button_exit = Button(menu, text="EXIT", bg="gray", height=3, width=30, command=menu.quit)

    button_database.grid(row=1, column=0, padx=5, pady=2)
    button_visualisation.grid(row=2, column=0, padx=5, pady=2)
    button_exit.grid(row=3, column=0, padx=5, pady=2)

def menu_labels(menu):
    # INIT LABEL
    Label(menu, text="Hello!", font=('Helvetica 20 bold'), bg="deep sky blue").grid(row=0, column=0, padx=0, pady=0)

def menu_init():
    #INIT tk
    menu = Tk()
    #USE SELFMADE FUNCTION
    menu_settings(menu)
    menu_buttons(menu)
    menu_labels(menu)
    #START
    menu.mainloop()