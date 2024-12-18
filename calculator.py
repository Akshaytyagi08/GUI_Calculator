import tkinter as tk

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry_label.config(text="Result:")
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry_label.config(text="Error:")
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Invalid Input")
    elif text == "C":
        entry_label.config(text="Input:")
        entry.delete(0, tk.END)
    else:
        entry_label.config(text="Input:")
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

# Label to indicate the current mode (Input or Result)
entry_label = tk.Label(root, text="Input:", font="Helvetica 15")
entry_label.grid(row=0, column=0, columnspan=4)

# Entry field for input and output
entry = tk.Entry(root, font="Helvetica 20", borderwidth=5, relief=tk.RIDGE)
entry.grid(row=1, column=0, columnspan=4, ipadx=5, ipady=5)

# Buttons for the calculator
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        btn = tk.Button(root, text=text, font="Helvetica 15", width=5, height=2)
        btn.grid(row=i + 2, column=j, padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()
 
