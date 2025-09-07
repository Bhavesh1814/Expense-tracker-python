import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",             
    password="your_password_here",  # <-- placeholder
    database="expense_tracker")
cursor = conn.cursor()
def add_expenses():
    category = input("Enter category (eg - Food, Travel)")
    amount = float(input("Enter amount"))
    date = input("Enter date (YYYY-MM-DD)")
    query = "INSERT INTO expenses(category,amount,date) VALUES(%s,%s,%s)"
    values=(category,amount,date)
    cursor.execute(query,values)
    conn.commit()
    print("Expense Added Successfully/n")

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    print("All expenses")
    for row in rows:
        print(row)
    print()

def monthly_summary():
    query = query = "SELECT DATE_FORMAT(date, '%M %Y') AS month, SUM(amount) AS monthly_spent FROM expenses GROUP BY month ORDER BY MIN(date);"
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Monthly Summary")
    for row in rows:
        print(row[0], ":", row[1])
    print()

def delete_expense():
    id_to_delete = input("Enter the ID of the expense to delete: ")
    cursor.execute("SELECT * FROM expenses WHERE id = %s", (id_to_delete,))
    result = cursor.fetchone()
    
    if result:
        cursor.execute("DELETE FROM expenses WHERE id = %s", (id_to_delete,))
        conn.commit()
        print("Expense deleted successfully!")
    else:
        print("Expense ID not found.")


while True:
    print("--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Monthly Summary")
    print("4. Delete Expense")
    print("5. Exit")
    
    choice = int(input("Choose an option: "))
    if choice == 1:
        add_expenses()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        monthly_summary()
    elif choice == 4:
        delete_expense()
    elif choice == 5:
        break
    else:
        print("Invalid choice")

conn.close()
