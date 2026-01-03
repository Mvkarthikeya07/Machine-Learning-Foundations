import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

# Save data to CSV
def save_expense():
    date = entry_date.get()
    desc = entry_desc.get()
    amount = entry_amount.get()

    if not date or not desc or not amount:
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        datetime.strptime(date, "%Y-%m-%d")
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Invalid date or amount format.")
        return

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, desc, amount])

    listbox.insert(tk.END, f"{date} - {desc} - ₹{amount}")
    entry_date.delete(0, tk.END)
    entry_desc.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

# Load all or filtered expenses
def filter_expenses():
    listbox.delete(0, tk.END)
    start = filter_start.get()
    end = filter_end.get()

    try:
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Error", "Enter valid start and end dates (YYYY-MM-DD).")
        return

    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row: continue
            date, desc, amount = row
            expense_date = datetime.strptime(date, "%Y-%m-%d")
            if start_date <= expense_date <= end_date:
                listbox.insert(tk.END, f"{date} - {desc} - ₹{amount}")

# Show graph
def show_graph():
    data = defaultdict(float)
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if not row: continue
                date, desc, amount = row
                month = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m")
                data[month] += float(amount)
    except FileNotFoundError:
        messagebox.showinfo("Info", "No expenses found.")
        return

    months = list(data.keys())
    totals = list(data.values())

    plt.bar(months, totals)
    plt.xlabel("Month")
    plt.ylabel("Total Spending (₹)")
    plt.title("Monthly Expense Summary")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# GUI setup
window = tk.Tk()
window.title("Expense Tracker with Filters and Graph")
window.geometry("500x600")

# Entry Fields
tk.Label(window, text="Date (YYYY-MM-DD):").pack()
entry_date = tk.Entry(window)
entry_date.pack()

tk.Label(window, text="Description:").pack()
entry_desc = tk.Entry(window)
entry_desc.pack()

tk.Label(window, text="Amount (₹):").pack()
entry_amount = tk.Entry(window)
entry_amount.pack()

tk.Button(window, text="Add Expense", command=save_expense).pack(pady=10)

# Filter Section
tk.Label(window, text="-- Filter Expenses --").pack(pady=5)
tk.Label(window, text="Start Date:").pack()
filter_start = tk.Entry(window)
filter_start.pack()
tk.Label(window, text="End Date:").pack()
filter_end = tk.Entry(window)
filter_end.pack()
tk.Button(window, text="Filter", command=filter_expenses).pack(pady=5)

# Expense List
listbox = tk.Listbox(window, width=60)
listbox.pack(pady=10)

# Graph Button
tk.Button(window, text="Show Monthly Spending Graph", command=show_graph).pack(pady=10)

window.mainloop()

