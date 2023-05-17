import tkinter as tk
from tkinter import messagebox



app=tk.Tk()
app.title("Automated App")
app.geometry('300x300')

def exit_app():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        app.destroy()

def button1_clicked():
    messagebox.showinfo("Button 1", "Button 1 clicked!")

def button2_clicked():
    messagebox.showinfo("Button 2", "Button 2 clicked!")

app.configure(bg="#f0f0f0")

button1 = tk.Button(app, text="Button 1", command=button1_clicked, bg="#4caf50", fg="white", font=("Arial", 14, "bold"))
button2 = tk.Button(app, text="Button 2", command=button2_clicked, bg="#2196f3", fg="white", font=("Arial", 14, "bold"))
exit_button = tk.Button(app, text="Exit", command=exit_app, bg="#f44336", fg="white", font=("Arial", 14, "bold"))


button1.pack(pady=10)
button2.pack(pady=10)
exit_button.pack(pady=10)








app.mainloop()