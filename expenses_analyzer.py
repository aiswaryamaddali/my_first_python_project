import pandas as pd
import matplotlib.pyplot as plt

def show_menu():
    print("\n--- Smart Expense Analyzer ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category-wise Total")
    print("4. Show Pie Chart")
    print("5. Exit")

def add_expense():
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category (Food/Travel/Shopping): ")
    amount = int(input("Amount: "))
    note = input("Note: ")

    with open("expenses.csv", "a") as f:
        f.write(f"\n{date},{category},{amount},{note}")
    print("Expense Added Successfully!")

def view_expenses():
    df = pd.read_csv("expenses.csv")
    print(df)

def category_total():
    df = pd.read_csv("expenses.csv")
    print(df.groupby("Category")["Amount"].sum())

def show_chart():
    df = pd.read_csv("expenses.csv")
    data = df.groupby("Category")["Amount"].sum()
    data.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Expense by Category")
    plt.show()

while True:
    show_menu()
    choice = input("Choose (1-5): ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        category_total()
    elif choice == "4":
        show_chart()
    elif choice == "5":
        print("Bye! Thanks for using!")
        break
    else:
        print("Wrong choice, try again!")