import tkinter as tk
from tkinter import ttk

def convert():
    try:
        # Get the user's input and convert it to float
        input_value = float(entry.get())
        input_value2 = float(entry2.get())

        # APY Conversion
        if unit_combobox.get() == "APY of USD":
            result = (input_value * 0.05116) / 12 * input_value2
            result_label.configure(text=f"{result:.2f} USD profit in a year.")
        elif unit_combobox.get() == "APY of EUR":
            result = (input_value * 0.034) / 12 * input_value2
            result_label.configure(text=f"{result:.2f} EUR profit in a year.")
        elif unit_combobox.get() == "APY of TRY":
            result = (input_value * 0.50) / 12 * input_value2
            result_label.configure(text=f"{result:.2f} TRY profit in a year.")
    except ValueError:
        result_label.configure(text="Wrong input")

# Main window
win = tk.Tk()
win.title("APY Calculator")
win.iconbitmap("C:/Python.png")  # Make sure the path to your icon file is correct
win.geometry("300x300+1200+200")
win.resizable(width=False, height=False)

# Create label frame
container = ttk.LabelFrame(win, text="APY Calculator", padding="10")
container.pack(padx=15, pady=15, fill="both", expand=True)

# Configure rows and columns
container.columnconfigure(index=0, weight=1)
container.columnconfigure(index=1, weight=2)
container.rowconfigure(index=0, weight=1)
container.rowconfigure(index=1, weight=1)
container.rowconfigure(index=2, weight=1)
container.rowconfigure(index=3, weight=1)

# Entry label and field
entry_label = ttk.Label(container, text="Enter Value:")
entry_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

entry = ttk.Entry(container)
entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

# Second entry label and field
entry_label2 = ttk.Label(container, text="Months Locked:")
entry_label2.grid(row=1, column=0, padx=5, pady=5, sticky="w")

entry2 = ttk.Entry(container)
entry2.grid(row=1, column=1, padx=5, pady=5, sticky="we")

# Combo box label and box
combo_label = ttk.Label(container, text="Convert")
combo_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

unit_combobox = ttk.Combobox(
    container,
    values=["APY of USD", "APY of EUR", "APY of TRY"],
    state="readonly"
)
unit_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="we")
unit_combobox.set("APY of TRY")

# Convert button
convert_button = ttk.Button(container, text="Convert", command=convert)
convert_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

# Create a new label frame for the result
result = ttk.LabelFrame(win, text="Result", padding="10")
result.pack(padx=15, pady=15, fill="both", expand=True)

# Inside the result frame
result_label = ttk.Label(result, text="")  # Label to display results
result_label.grid(row=0, column=0, padx=5, pady=5)

# Start the main loop
win.mainloop()
