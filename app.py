import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import main

def git_repo_create():
    global root
    username = username_entry.get()
    password = password_entry.get()
    projectname=projectname_entry.get()
    description = description_entry.get()
    repotype=repotype_var.get()
    if username=="" or password=="" or projectname=="":
        messagebox.showerror("Alert","Please fill data as required")
    else:
        main.github_repo_create(username, password, projectname, description, repotype)
        messagebox.showinfo(title="Git commands use", message=f"https://github.com/{username}/{projectname}/.git")


root = tk.Tk()
root.title("Github Automation")
root.geometry('250x300')

# Create entry boxes
username_label = tk.Label(root, text="Username:")
username_entry = tk.Entry(root)

password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root,show="*")

projectname_label = tk.Label(root, text="Project Name(unique):")
projectname_entry = tk.Entry(root)


description_label = tk.Label(root, text="Description(Optional):")
description_entry = tk.Entry(root)

# Create dropdown menu
repotype_label = tk.Label(root, text="Repo Type:")
repotype_var = tk.StringVar(root)
repotype_dropdown = ttk.Combobox(root, textvariable=repotype_var)
repotype_dropdown['values'] = ('Public','Private')
repotype_dropdown.current(0)


username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
projectname_label.pack()
projectname_entry.pack()
description_label .pack()
description_entry.pack()
repotype_label.pack()
repotype_dropdown.pack()


# Create button
submit_button = tk.Button(root, text="Create Repository", command=git_repo_create)
submit_button.pack()

# Run the application
root.mainloop()
