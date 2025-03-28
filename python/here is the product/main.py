from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("600x400")

lbl = Label(text="Product of two numbers")

num1 = Entry(root, width=10)
num2 = Entry(root, width=10)

def multiply():
    try:
        n1 = float(num1.get())
        n2 = float(num2.get())
        result = n1 * n2
        lbl.config(text=f"Result: {result}")
    except ValueError:
        lbl.config(text="Invalid input!")

btn= Button(root, text="Multiply", command=multiply)

lbl.pack(pady=10)
num1.pack(pady=10)
num2.pack(pady=10)
btn.pack(pady=10)

root.mainloop()