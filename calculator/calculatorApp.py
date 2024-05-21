import tkinter as tk


class Calculator:
    """define a calculator app section"""

    def __init__(self, root):
        self.root = root
        self.root.title("CalculatorAPP +V_[1.1.1]")
        self.root.geometry("350x450")
        self.root.configure(bg="black")

        self.expression = ""
        self.text_input = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        """Entry widget for displaying the expression"""
        self.entry = tk.Entry(
            self.root,
            font=("arial", 20, "normal"),
            textvariable=self.text_input,
            bd=5,
            insertwidth=5,
            width=20,
            borderwidth=4,
            relief="sunken",
        )
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        # Button creation and placement
        buttons = [
            ("Clear (CE)", 1, 0, "orange", 2, 1),
            ("+", 1, 2, "gray", 1, 1),
            ("x", 1, 3, "gray", 1, 1),
            ("7", 2, 0, "lightblue", 1, 1),
            ("8", 2, 1, "lightblue", 1, 1),
            ("9", 2, 2, "lightblue", 1, 1),
            ("-", 2, 3, "gray", 1, 1),
            ("4", 3, 0, "lightblue", 1, 1),
            ("5", 3, 1, "lightblue", 1, 1),
            ("6", 3, 2, "lightblue", 1, 1),
            ("+", 3, 3, "gray", 1, 1),
            ("1", 4, 0, "lightblue", 1, 1),
            ("2", 4, 1, "lightblue", 1, 1),
            ("3", 4, 2, "lightblue", 1, 1),
            ("=", 4, 3, "lightgreen", 1, 2),  # Span 2 rows
            ("0", 5, 0, "lightblue", 2, 1),
            (".", 5, 2, "lightblue", 1, 1),
        ]

        for text, row, col, color, colspan, rowspan in buttons:
            self.create_button(text, row, col, color, colspan, rowspan)

    def create_button(self, text, row, col, color, colspan=1, rowspan=1):
        """create buttons"""
        button = tk.Button(
            self.root,
            text=text,
            padx=20,
            pady=20,
            font=("arial", 18, "bold"),
            bg=color,
            command=lambda: self.on_button_click(text),
        )
        button.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan, sticky="nsew")

    def on_button_click(self, char):
        if char == "Clear (CE)":
            self.expression = ""
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        else:
            self.expression += str(char).replace("x", "*")

        self.text_input.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)

    # Make the buttons resize properly when the window is resized
    for i in range(6):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()
