import json 

expenses = []
def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
    "amount": amount,
    "category": category,
    "description": description
    }

    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!\n")

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def load_expenses():
    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
                    
    except FileNotFoundError:       #try block might fail with first run
        expenses = []               # if expenses.json doesn't exist

load_expenses()

def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return

    print("===== Expenses List =====")

    for expense in expenses:
        print(f"Category: {expense['category']}")
        print(f"Description: {expense['description']}")
        print(f"Amount: {expense['amount']}")
        print("--------------------")

def view_total():
    if not expenses:
        print("No expenses found.\n")
        return

    total = 0

    for expense in expenses:
        total += int(expense["amount"])
    
    print(f"Total Expenses: {total}\n")

def search_by_category():
    category = input("Enter category to search: ")

    found = False
    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")
            print(f"Amount: {expense['amount']}")
            print("--------------------")

            found = True
    if not found:
        print("No expenses found for this category.\n")

def display_menu():
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Search by Category")
    print("5. Exit")

running = True

while running:
    display_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        view_total()

    elif choice == "4":
        search_by_category()

    elif choice == "5":
        print("Goodbye!\n")
        running = False

    else:
        print("Invalid option.\n")

