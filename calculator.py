import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI 计算器")
        self.root.resizable(False, False)

        self.expression = ""

        self.display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")
        self.display.insert(0, "0")

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        for r, row in enumerate(buttons, start=1):
            for c, char in enumerate(row):
                tk.Button(root, text=char, font=("Arial", 20), width=5, height=2,
                          command=lambda ch=char: self.on_button_click(ch)).grid(row=r, column=c, padx=5, pady=5)

        tk.Button(root, text="清除", font=("Arial", 20), width=11, height=2, command=self.clear).grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        tk.Button(root, text="退出", font=("Arial", 20), width=11, height=2, command=root.quit).grid(row=5, column=2, columnspan=2, padx=5, pady=5)

        root.bind("<Return>", lambda event: self.calculate())
        root.bind("<BackSpace>", lambda event: self.backspace())

    def on_button_click(self, char):
        if char == "=":
            self.calculate()
            return

        if self.display.get() == "0" and char not in ".+*/-":
            self.display.delete(0, tk.END)

        self.display.insert(tk.END, char)

    def calculate(self):
        try:
            expression = self.display.get()
            expression = expression.replace("×", "*").replace("÷", "/")
            result = str(eval(expression))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, "错误")

    def clear(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, "0")

    def backspace(self):
        current = self.display.get()
        if len(current) > 1:
            self.display.delete(len(current) - 1, tk.END)
        else:
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
