import csv
from datetime import datetime

expenses = []

def show_menu():
   
    print("========================")
    print("     EXPENSE TRACKER    ")
    print("========================")
    print("1. Add expense")
    print("2. View Expenses")
    print("3. Search Expenses")
    print("4. Delete Expense")
    print("5. Show Total")
    print("6. Exit")
    print("========================")
    try:

        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("Please enter your choice in number.")
        return 0

def add_expense():

    date = input("Enter date: ").strip()
    if not date:
        print("Date cannot be empty")
        return
    try: 
        datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        print("Enter a valid date. (05-01-2026)")
        return
    
    category = input("Enter your category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return
    description = input("Enter your description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return

    try:
        amount = int(input("Enter your amount: "))
        if amount <=0:
            print("Enter a valid amount.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    expense = {
    "Date": date,
    "Category": category,
    "Description": description,
    "Amount": amount
}
    
    expenses.append(expense)
    save_expenses()
    print("Expense added successfully")

def view_expenses(): 

    for expense in expenses:
        display_expense(expense)
    if not expenses:
        print("No expenses found. Please add an expense.")

def search_expenses():
    if not expenses:
        print("No expenses found. Please add an expense.")
        return

    search_category = input("Enter category to search: ").strip().lower()
    found = False

    for expense in expenses:

        if expense["Category"].lower() == search_category:
            
            display_expense(expense)

            found = True

    if not found:
        print("Expense not found.")

def delete_expenses():

    if not expenses:
        print("Add expense please.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(number, "-", expense["Category"], "-", expense["Description"], "-", expense["Amount"])
    try:
        expense_number = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Enter a valid expense number.")
        return
    if expense_number >= 1 and expense_number <= len(expenses):

        expenses.pop(expense_number - 1)
        save_expenses()

        print("Expense deleted successfully.")

    else:

        print("Invalid expense number.")

def show_total():

    total = 0
    if not expenses:
        print("No expenses found.")
        return
    for expense in expenses:
        total += expense["Amount"]
    print("Total:", total)

def display_expense(expense):
        
        print("Date:", expense["Date"])
        print("Category:", expense["Category"])
        print("Description:", expense["Description"])
        print("Amount:", expense["Amount"])

def save_expenses():
    try:

        with open("expenses.csv", "w", newline="") as file:

            writer = csv.DictWriter(file, fieldnames=["Date", "Category", "Description", "Amount"])
            writer.writeheader()
            writer.writerows(expenses)
    except OSError:
        print("Could not save expenses.")
    
def load_expenses():

    try:
        with open("expenses.csv", "r", newline="") as file:

            reader = csv.DictReader(file)

            for expense in reader:
                try:

                    expense["Amount"] = int(expense["Amount"])
                    expenses.append(expense)
                except ValueError:
                    print("Invalid amount found in CSV. Skipping this expense.")
                    continue

    except FileNotFoundError:
        print("File not found. Please add expense.")

load_expenses()

while True:

    choice = show_menu()

    if choice == 1:

        add_expense()

    elif choice == 2:

        view_expenses()

    elif choice == 3:

        search_expenses()

    elif choice == 4:

        delete_expenses()

    elif choice == 5:

        show_total()

    elif choice == 6:
        break

    else:

        print("Invalid choice. Please choose 1-6")

