from matplotlib import pyplot as plt
import sqlite3

def create_list_per_category(dev_y):
    # DO LIST OF TOTAL EXPENSES FOR EACH CATEGORY
    list_all = []
    dev_y.clear()
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()

    categories = [("Grocery shopping",), ("Food from restaurant",), ("Car fuel",),
                  ("Car extra expenses",), ("Investments",), ("Gifts and loan",), ("Clothes",), ("House",),
                  ("Subscription",), ("Extra",)]

    for category in categories:
        c.execute("SELECT amount FROM expenses WHERE category=?", category)

        records = c.fetchall()

        for record in records:
            list_all.append(int(record[0]))

        expresion = str(sum(list_all))
        dev_y.append(expresion)
        list_all.clear()

    conn.commit()
    conn.close()
    # CONVERT DEV_Y TO INT
    for i in range(0, len(dev_y)):
        dev_y[i] = int(dev_y[i])

    return dev_y


def create_list_per_month(dev_y):
    # DO LIST OF TOTAL EXPENSES FOR EACH MONTH
    list_all = []
    dev_y.clear()
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()

    months = [("January",), ("February",), ("March",), ("April",), ("May",),
              ("June",), ("July",), ("August",), ("September",), ("October",), ("November",), ("December",)]

    for month in months:
        c.execute("SELECT amount FROM expenses WHERE month=?", month)

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
    # SHOW A BAR OF EXPENSES FOR EACH MONTH
    dev_x = ["Jan", "Feb", "Mar", "Apr", "May",
             "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
    dev_y = []

    create_list_per_month(dev_y)

    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.title("Expenses per month")

    plt.bar(dev_x, dev_y)
    plt.show()


def show_category_bar():
    # SHOW A BAR OF EXPENSES FOR EACH CATEGORY
    dev_x = ["Grocery", "Dinner", "Car fuel",
             "Car extra", "Investments", "Gifts", "Clothes", "House", "Subscription", "Extra"]

    dev_y = []

    create_list_per_category(dev_y)
    plt.figure(figsize=(12, 6))

    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title("Expenses per category")

    plt.bar(dev_x, dev_y)
    plt.show()
