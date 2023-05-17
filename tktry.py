import tkinter as tk
from tkinter import ttk

def submit():
    name = name_entry.get()
    age = age_entry.get()
    country = country_var.get()
    print(f"Name: {name}\nAge: {age}\nCountry: {country}")

# Create the main window
root = tk.Tk()
root.title("User Information")

# Create entry boxes
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)

age_label = tk.Label(root, text="Age:")
age_entry = tk.Entry(root)

name_label.pack()
name_entry.pack()
age_label.pack()
age_entry.pack()

# Create dropdown menu
country_label = tk.Label(root, text="Country:")
country_var = tk.StringVar(root)
country_dropdown = ttk.Combobox(root, textvariable=country_var)
country_dropdown['values'] = ('USA', 'Canada', 'UK', 'Australia', 'India')
country_dropdown.current(0)

country_label.pack()
country_dropdown.pack()

# Create button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Run the application
root.mainloop()
