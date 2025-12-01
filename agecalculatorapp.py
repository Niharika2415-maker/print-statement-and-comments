import tkinter as tk
from datetime import date

# Function to calculate age
def calculate_age():
    name = name_entry.get()
    d = int(date_entry.get())
    m = int(month_entry.get())
    y = int(year_entry.get())

    today = date.today()
    age = today.year - y

    # adjust if birthday hasn't happened yet this year
    if (today.month, today.day) < (m, d):
        age -= 1

    message = f"Hello {name}! You are {age} years old."
    result_label.config(text=message)


# Main window
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")

# Title Label
title = tk.Label(root, text="Age Calculator App", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Frame for entries (side-by-side)
frame = tk.Frame(root)
frame.pack(pady=10)

# Name
tk.Label(frame, text="Name: ").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1)

# Date
tk.Label(frame, text="date: ").grid(row=1, column=0, sticky="e")
date_entry = tk.Entry(frame)
date_entry.grid(row=1, column=1)

# Month
tk.Label(frame, text="Month: ").grid(row=2, column=0, sticky="e")
month_entry = tk.Entry(frame)
month_entry.grid(row=2, column=1)

# Year
tk.Label(frame, text="Year: ").grid(row=3, column=0, sticky="e")
year_entry = tk.Entry(frame)
year_entry.grid(row=3, column=1)

# Button
btn = tk.Button(root, text="Calculate Age", command=calculate_age)
btn.pack(pady=15)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
