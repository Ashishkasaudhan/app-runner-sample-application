import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Welcome App")

# Create a function to handle the button click
def on_submit():
    name = name_entry.get()
    if name:
        messagebox.showinfo("Welcome", f"Welcome, {name}!")
    else:
        messagebox.showwarning("Input Error", "Please enter your name.")

# Create and place the widgets
tk.Label(root, text="Enter your name:").pack(pady=10)

name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

tk.Button(root, text="Submit", command=on_submit).pack(pady=20)

# Run the application
root.mainloop()
