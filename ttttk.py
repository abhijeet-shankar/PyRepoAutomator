import tkinter as tk
from tkinter import ttk
import tkinter.font

# Create the main window
root = tk.Tk()
root.title("My App")

# Create a frame to hold the widgets
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Create the first entry box
label_1 = tk.Label(frame, text="Enter value 1:")
label_1.grid(row=0, column=0, sticky=tk.W)
entry_1 = tk.Entry(frame, width=20)
entry_1.grid(row=0, column=1)

# Create the second entry box
label_2 = tk.Label(frame, text="Enter value 2:")
label_2.grid(row=1, column=0, sticky=tk.W)
entry_2 = tk.Entry(frame, width=20)
entry_2.grid(row=1, column=1)

# Create the dropdown menu
label_3 = tk.Label(frame, text="Select operation:")
label_3.grid(row=2, column=0, sticky=tk.W)
options = ["Add", "Subtract", "Multiply", "Divide"]
dropdown = ttk.Combobox(frame, values=options, width=17, state="readonly")
dropdown.current(0)
dropdown.grid(row=2, column=1)

# Create the button
def calculate():
    value_1 = int(entry_1.get())
    value_2 = int(entry_2.get())
    operation = dropdown.get()

    if operation == "Add":
        result = value_1 + value_2
    elif operation == "Subtract":
        result = value_1 - value_2
    elif operation == "Multiply":
        result = value_1 * value_2
    elif operation == "Divide":
        result = value_1 / value_2

    result_label.configure(text="Result: " + str(result))

calculate_button = tk.Button(frame, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create the result label
result_label = tk.Label(frame, text="Result:")
result_label.grid(row=4, column=0, columnspan=2)

# Set the background color and font style
frame.configure(background="#f2f2f2")
tk.font.nametofont("TkDefaultFont").configure(size=12)

# Start the main loop
root.mainloop()
