import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import main

def git_repo_create():
    global root
    username = username_entry.get()
    password = password_entry.get()
    projectname=projectname_entry.get()
    description = description_entry.get('1.0', tk.END)
    print(description)
    repotype=repotype_var.get()
    if username=="" or password=="" or projectname=="":
        messagebox.showerror("Alert","Please fill data as required")
    else:
        main.github_repo_create(username, password, projectname, description, repotype)
        messagebox.showinfo(title="Git commands use", message=f"https://github.com/{username}/{projectname}/.git")


root = tk.Tk()
root.title("Github Automation")
root.geometry('350x360')
root.resizable(0,0)
root.configure(background='#FFFAF0')

username_label = tk.Label(root, text="Username:",pady=20,background='#FFFAF0')
username_entry = tk.Entry(root,width=25)

password_label = tk.Label(root, text="Password:",pady=20,background='#FFFAF0')
password_entry = tk.Entry(root,show="*",width=25)

projectname_label = tk.Label(root, text="Project Name(unique):",background='#FFFAF0')
projectname_entry = tk.Entry(root,width=25)


description_label = tk.Label(root, text="Description(Optional):",pady=20,background='#FFFAF0')
# description_entry = tk.Entry(root)
description_entry = tk.Text(root, height=3, width=19)

# Create dropdown menu
repotype_label = tk.Label(root, text="Repo Type:",pady=20,background='#FFFAF0')
repotype_var = tk.StringVar(root)
repotype_dropdown = ttk.Combobox(root, textvariable=repotype_var,state='readonly',width=25)
repotype_dropdown['values'] = ('Public','Private')
repotype_dropdown.current(0)


username_label.grid(row=0,column=1)
username_entry.grid(row=0,column=2)
root.rowconfigure(0, minsize=35, weight=4)

password_label.grid(row=1,column=1)
password_entry.grid(row=1,column=2)
root.rowconfigure(1, minsize=35, weight=4)

projectname_label.grid(row=2,column=1)
projectname_entry .grid(row=2,column=2)
root.rowconfigure(2, minsize=45, weight=4)

description_label.grid(row=3,column=1)
description_entry.grid(row=3,column=2)
root.rowconfigure(3, minsize=45, weight=4)

repotype_label.grid(row=4,column=1,pady=20)
repotype_dropdown.grid(row=4,column=2)
root.rowconfigure(4, minsize=35, weight=4)
# Create button
submit_button = tk.Button(root, text="Create Repository", command=git_repo_create,activebackground="green",background="dark blue",foreground='white',width=13)
submit_button.grid(row=5,column=0,columnspan=3)

exit_button = tk.Button(root, text="Exit", command=root.destroy,foreground='white',background="red",width=3)
exit_button.grid(row=5,column=2,columnspan=7)
root.rowconfigure(5, minsize=15, weight=4)


# Run the application
root.mainloop()


