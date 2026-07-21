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
        print("View Expenses - Coming Soon!\n")

    elif choice == "3":
        print("View Total - Coming Soon!\n")

    elif choice == "4":
        print("Search Category - Coming Soon!\n")

    elif choice == "5":
        print("Goodbye!\n")
        running = False

    else:
        print("Invalid option.\n")

