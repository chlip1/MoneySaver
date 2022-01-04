from tkinter import *
from database import *
from visualisation import *

def menu_settings(menu):
    # SETTINGS
    menu.configure(bg="lightgray")
    menu.title("MENU")
    menu.geometry("230x160")

def menu_buttons(menu):
    # INIT BUTTONS
    button_database = Button(menu, text="Add a expenditure", bg="gray", height=1, width=30, command=lambda: database.gui_database_creator(menu))
    button_visualisation = Button(menu, text="Show past expenditures", bg="gray", height=1, width=30, command=lambda: gui_visualisation_creator(menu))
    button_exit = Button(menu, text="EXIT", bg="gray", height=1, width=30, command=menu.quit)
    #SHOW BUTTONS
    button_database.grid(row=1, column=0, padx=5, pady=2)
    button_visualisation.grid(row=2, column=0, padx=5, pady=2)
    button_exit.grid(row=4, column=0, padx=5, pady=2)

def menu_labels(menu):
    # INIT LABEL
    Label(menu, text="Hello!", font=('Helvetica 20 bold'), bg="lightgray").grid(row=0, column=0, padx=0, pady=0)

def menu_init():
    #INIT tk
    menu = Tk()
    #USE SELFMADE FUNCTION
    menu_settings(menu)
    menu_buttons(menu)
    menu_labels(menu)
    #START
    menu.mainloop()

if __name__ == "__main__":

    menu_init()
