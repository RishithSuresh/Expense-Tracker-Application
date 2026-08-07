# Expense Tracker

This Python program is a menu-driven Expense Tracker that helps users record, view, and summarize their daily expenses. It stores expense data permanently in a CSV (Comma-Separated Values) file, allowing the records to remain available even after the program is closed.

The program first checks whether the expenses.csv file exists. If it does not, it automatically creates the file and adds the required column headers: Date, Category, Amount, and Note.

The application provides the following features:

Add Expense:
The user enters the expense date, category, amount, and an optional note. The program validates the date format (YYYY-MM-DD) and ensures that the amount entered is greater than zero before saving the record to the CSV file.
View All Expenses:
Displays all recorded expenses in a neatly formatted table showing the date, category, amount, and note. It also calculates and displays the total amount spent by summing all recorded expenses.
Category-wise Summary:
Groups expenses based on their categories (such as Food, Travel, Shopping, etc.) and calculates the total spending for each category. This helps users understand where most of their money is being spent.
Exit:
Allows the user to safely terminate the program.

The program uses functions to organize different tasks, making the code modular and easier to maintain. It also includes exception handling to manage invalid inputs such as incorrect date formats or non-numeric amounts, preventing the program from crashing.