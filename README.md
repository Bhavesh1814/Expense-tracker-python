Expense Tracker Python

A simple Python-based expense tracker using MySQL, designed to help you keep track of your daily, monthly, and yearly expenses with ease.

Features
->Add, view, modify, and delete expenses
->Categorize expenses (Food, Travel, Shopping, etc.)
->View monthly and yearly summaries
->Optionally display expenses in a neat table format

Setup Instructions
1. Clone the repository
git clone https://github.com/Bhavesh1814/Expense-tracker-python.git
cd Expense-tracker-python

2. Install required Python packages
pip install mysql-connector-python tabulate

3. Setup the MySQL database

Log in to your MySQL server and run:

CREATE DATABASE expense_tracker;

USE expense_tracker;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50),
    amount FLOAT,
    description VARCHAR(255),
    date DATE
);

4. Update database credentials

In expense_tracker.py, update these lines with your MySQL username and password:

conn = mysql.connector.connect(
    host="localhost",
    user="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    database="expense_tracker"
)

How to Run
python expense_tracker.py


The menu will appear:

Choose an option:
1. Add Expense
2. View Expenses
3. Modify Expense
4. Delete Expense
5. Monthly Summary
6. Exit

Usage Example

Add an expense:

Category: Food

Amount: 250

Description: Lunch

Date: 2025-09-07

View monthly summary:

Month	Total Expense
August 2025	680.0
September 2025	1370.0

Future Improvements
->GUI interface (Tkinter or PyQt)
->Export data to CSV
->Add charts/graphs for visual analysis
->Notifications for budget limits

License

This project is open to all. You can freely use, modify, and distribute it for personal or commercial purposes.


