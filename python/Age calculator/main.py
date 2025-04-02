from tkinter import *
from datetime import datetime

def calculate_age():
    try:
        birth_year = int(year_entry.get())
        birth_month = int(month_entry.get())
        birth_day = int(day_entry.get())
        birth_date = datetime(birth_year, birth_month, birth_day)
        today = datetime.now()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

root = Tk()
root.geometry("400x400")
root.title("Age Calculator")

frame = Frame(master=root, height=200, width=360, bg="blue")
frame.pack(pady=20)

lbl = Label(frame, text="Enter your birth year:", bg="#3895D3", fg="white")
lbl.grid(row=0, column=0, padx=10, pady=5)
year_entry = Entry(frame, width=20, bg="white", fg="black")
year_entry.grid(row=0, column=1, padx=10, pady=5)

lbl2 = Label(frame, text="Enter your birth month:", bg="#3895D3", fg="white")
lbl2.grid(row=1, column=0, padx=10, pady=5)
month_entry = Entry(frame, width=20, bg="white", fg="black")
month_entry.grid(row=1, column=1, padx=10, pady=5)

lbl1 = Label(frame, text="Enter your birth day:", bg="#3895D3", fg="white")
lbl1.grid(row=2, column=0, padx=10, pady=5)
day_entry = Entry(frame, width=20, bg="white", fg="black")
day_entry.grid(row=2, column=1, padx=10, pady=5)

calculate_button = Button(frame, text="Calculate Age", command=calculate_age, bg="#4CAF50", fg="white")
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = Label(root, text="", bg="white", fg="black", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()