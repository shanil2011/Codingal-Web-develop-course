import tkinter as tk

window = tk.Tk()
window.title("Interest Rate Calculator")
window.resizable(width=False, height=False)

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())
        interest = (principal * rate * time) / 100
        result_label.config(text=f"Interest: ${interest:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

def clear_fields():
    principal_entry.delete(0, tk.END)
    rate_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    result_label.config(text="")

principal_entry = tk.Entry(window, width=20)
principal_entry.grid(row=0, column=1, padx=10, pady=5)

rate_entry = tk.Entry(window, width=20)
rate_entry.grid(row=1, column=1, padx=10, pady=5)

time_entry = tk.Entry(window, width=20)
time_entry.grid(row=2, column=1, padx=10, pady=5)

time_label = tk.Label(window, text="Time (years):")
time_label.grid(row=2, column=0, padx=10, pady=5)

result_label = tk.Label(window, text="Principal Amount:")
result_label.grid(row=0, column=0, padx=10, pady=5)

result_label = tk.Label(window, text="Interest: $0.00")
result_label.grid(row=0, column=0, padx=20, pady=10)

rate_label = tk.Label(window, text="Rate of Interest (%):")
rate_label.grid(row=1, column=0, padx=10, pady=5)

btn_convert = tk.Button(window, text="Calculate Interest", command=calculate_interest)
btn_convert.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

window.mainloop()
