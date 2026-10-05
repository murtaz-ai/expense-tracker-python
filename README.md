# Expense Tracker

A simple command-line Expense Tracker built with Python.
The application allows users to add, view, search, delete, and calculate the total of their expenses.

Expenses are stored in a CSV file so the data remains available even after closing the program.

## Features

* Add new expenses
* View all expenses
* Search expenses by category
* Delete expenses
* Calculate total expenses
* Validate user input
* Validate dates
* Handle invalid amounts
* Save expenses to CSV
* Load saved expenses when the program starts
* Handle missing or invalid CSV data

## Technologies Used

* Python
* CSV module
* Datetime module
* Lists
* Dictionaries
* Functions
* File Handling
* Exception Handling

## Project Structure

```text
ExpenseTracker/
│
├── expense_tracker.py
├── expenses.csv
└── README.md
```

> `expenses.csv` is created automatically when expenses are saved.

## How to Run

Make sure Python is installed on your system.

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Go to the project directory:

```bash
cd ExpenseTracker
```

Run the program:

```bash
python expense_tracker.py
```

## Menu

```text
========================
     EXPENSE TRACKER
========================
1. Add expense
2. View Expenses
3. Search Expenses
4. Delete Expense
5. Show Total
6. Exit
========================
```

## Data Storage

Expenses are stored in `expenses.csv` using Python's built-in `csv` module.

Each expense contains:

* Date
* Category
* Description
* Amount

Example:

```text
Date,Category,Description,Amount
05-10-2026,Food,Lunch,350
05-10-2026,Transport,Bus,100
```

## Input Validation

The application checks for:

* Empty fields
* Invalid dates
* Invalid amounts
* Zero or negative amounts
* Invalid menu choices
* Invalid expense numbers

## Learning Goals

This project was built to practice fundamental Python concepts including:

* Functions
* Lists and dictionaries
* Loops and conditions
* File handling
* CSV data handling
* Exception handling
* Input validation
* Working with dates

## Future Improvements

Possible future improvements include:

* Monthly expense summaries
* Expense categories summary
* Better terminal formatting
* Export reports
* Data visualization
* GUI version

## Author

**Muhammad Murtaz**

BS Artificial Intelligence Student
Interested in AI, Machine Learning, Robotics, and Software Development.
