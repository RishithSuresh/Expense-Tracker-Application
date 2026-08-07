import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"


# Function to create CSV file if it doesn't exist
def create_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])


# Function to add a new expense
def add_expense():
    try:
        date = input("Enter Date (YYYY-MM-DD): ")

        # Validate date format
        datetime.strptime(date, "%Y-%m-%d")

        category = input("Enter Category: ")

        amount = float(input("Enter Amount: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        note = input("Enter Note (Optional): ")

        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, note])

        print("Expense added successfully!")

    except ValueError:
        print("Invalid input! Please enter valid data.")


# Function to view all expenses
def view_expenses():
    total = 0
    found = False

    print("\n---------------- Expense Records ----------------")
    print("{:<12} {:<15} {:<10} {:<20}".format("Date", "Category", "Amount", "Note"))

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            found = True
            print("{:<12} {:<15} {:<10} {:<20}".format(row[0], row[1], row[2], row[3]))
            total += float(row[2])

    if not found:
        print("No expenses found.")

    print("-----------------------------------------------")
    print("Total Amount Spent: ₹", total)


# Function to display category-wise summary
def category_summary():
    summary = {}

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            category = row[1]
            amount = float(row[2])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    if len(summary) == 0:
        print("No expense records available.")
        return

    print("\n------ Category Wise Spending ------")
    for category in summary:
        print(category, ":", "₹", summary[category])


# Main Program
create_file()

while True:
    print("\n========== Expense Tracker ==========")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category Wise Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        category_summary()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")