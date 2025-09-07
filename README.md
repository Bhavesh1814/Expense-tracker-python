# Expense Tracker - Python + MySQL

A simple **Python + MySQL** project to track personal expenses.  
This project allows you to **add, view, modify, and delete expenses** easily from the console. It's beginner-friendly and a great way to learn Python and MySQL integration.

---

## Features

- **Add Expenses:** Enter category, amount, and date.  
- **View Expenses:** See all your expenses in a neat table format.  
- **Modify Expenses:** Update existing expense records.  
- **Delete Expenses:** Remove unwanted expense entries.  
- **Monthly Summary:** (Optional) View total expenses per month.

---

## Setup Instructions

1. **Install Python** (3.7+ recommended) and **MySQL** on your system.  

2. **Create a MySQL Database**:

```sql
CREATE DATABASE expense_tracker;
USE expense_tracker;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50),
    amount FLOAT,
    date DATE
);
