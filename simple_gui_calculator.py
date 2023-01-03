
#Author: Filip Navrkal

import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create the display widget
        self.display = tk.Entry(self, font=("Helvetica", 20), justify="right", bd=16, bg="lightgray")
        self.display.grid(row=0, columnspan=4, sticky="nsew")

        # Create the buttons
        buttons = [
            ["AC", "C", "CE", "±"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["(", ")", "", ""]
        ]
        for i, row in enumerate(buttons, start=1):
            for j, button in enumerate(row):
                cmd = lambda x=button: self.click(x)
                tk.Button(self, text=button, font=("Helvetica", 14), bg="#f0f0f0", activebackground="#d9d9d9", width=8, height=4, command=cmd).grid(row=i, column=j, sticky="nsew")

        # Make the buttons expand with the window
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

    def click(self, key):
        if key == "=":
            # Evaluate the expression and display the result
            result = eval(self.display.get())
            self.display.delete(0, "end")
            self.display.insert(0, result)
        elif key == "AC":
            # Clear the display
            self.display.delete(0, "end")
        elif key == "C":
            # Clear the current entry in the display
            self.display.delete(len(self.display.get()) - 1)
        elif key == "CE":
            # Clear the current entry in the display
            self.display.delete(0, "end")
        elif key == "±":
            # Change the sign of the current entry in the display
            if self.display.get()[0] == "-":
                self.display.delete(0)
            else:
                self.display.insert(0, "-")
        else:
            # Add the key to the display
            self.display.insert("end", key)

if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop() 
