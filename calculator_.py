import tkinter as tk

# Function to perform the calculation
def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)

# Create a GUI window
window = tk.Tk()
window.title("Basic Calculator")

# Entry field for display
entry = tk.Entry(window, font=('Arial', 18), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 16), command=calculate).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 16), command=clear_entry).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 16), command=lambda value=button: button_click(value)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the GUI event loop
window.mainloop()
