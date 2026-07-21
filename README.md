# Command Line Expense Tracker

A simple command-line expense tracker built using Python. The application allows users to add expenses, view saved expenses, calculate total spending, and search expenses by category. Data is stored locally using a JSON file so expenses remain available even after closing the program.

This project was developed while practicing real-world Git workflows using feature branches, commits, and pull requests.

---

## Features

- Add new expenses
- Save expenses permanently to a JSON file
- Load previous expenses when the program starts
- View all recorded expenses
- Calculate total expenses
- Search expenses by category
- Command-line menu interface
- Handles empty expense lists safely

---

## Technologies Used

- Python 3
- JSON for data storage
- Git and GitHub for version control

---

## Project Structure

```
expense-tracker/
│
├── expense-tracker.py     # Main application file
├── expenses.json          # Stores expense data (generated automatically)
├── .gitignore             # Prevents personal data files from being tracked
└── README.md              # Project documentation
```

---

## How It Works

The application starts with a command-line menu:

```
===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. View Total
4. Search by Category
5. Exit
```

The user selects an option, and the program performs the requested operation.

---

## Features Explained

### 1. Add Expense

Users can enter:

- Amount
- Category
- Description

Example:

```
Enter amount: 500
Enter category: Food
Enter description: Lunch
```

The expense is stored as a dictionary:

```python
{
    "amount": "500",
    "category": "Food",
    "description": "Lunch"
}
```

---

### 2. Save and Load Expenses

Expenses are stored in `expenses.json`.

Example:

```json
[
    {
        "amount": "500",
        "category": "Food",
        "description": "Lunch"
    }
]
```

The program loads existing expenses when it starts and saves new expenses automatically.

---

### 3. View Expenses

Displays all saved expenses:

Example:

```
===== Expenses List =====

Category: Food
Description: Lunch
Amount: 500
--------------------
```

---

### 4. View Total Expenses

Calculates the total amount spent.

Example:

```
Total Expenses: 800
```

The program converts stored string values into integers before performing calculations.

---

### 5. Search by Category

Allows users to find expenses belonging to a specific category.

Example:

```
Enter category to search: Food
```

Output:

```
Category: Food
Description: Lunch
Amount: 500
```

The search is case-insensitive, so `food` and `Food` return the same results.

---

## Running the Project

### Clone the repository

```bash
git clone <repository-url>
```

### Navigate into the project folder

```bash
cd expense-tracker
```

### Run the application

```bash
python expense-tracker.py
```

---

## Git Workflow Used

Each feature was developed in a separate branch and merged through a pull request.

Branches created:

```
feature/menu
feature/add-expense
feature/save-to-file
feature/view-expenses
feature/total-expenses
feature/search-category
```

Workflow:

```
Create Feature Branch
        ↓
Develop Feature
        ↓
Commit Changes
        ↓
Push Branch
        ↓
Create Pull Request
        ↓
Merge into Main
        ↓
Delete Feature Branch
```

---

## Future Improvements

Possible features that can be added:

- Input validation for incorrect values
- Delete expenses
- Edit existing expenses
- Add expense dates
- Export reports
- Convert project into an Object-Oriented design
- Add unit tests

---

## Learning Outcomes

Through this project, I practiced:

- Python functions
- Lists and dictionaries
- Loops and conditions
- File handling
- JSON data storage
- Exception handling
- Git branching strategy
- Pull requests and code merging

---

## Author

Filza Syed