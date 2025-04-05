import tkinter as tk

window = tk.Tk()

window.title("Legnth Converter")

window.resizable(width=False, height=False)

def inches_to_cm():


inches = ent_inches.get()

cm = 2.54 * (float(inches))

lbl_result["text"] = f"{cm}"

frm_entry = tk.Frame(master=window)

ent_inches = tk.Entry(master=frm_entry, width=10)

lbl_inches = tk.Label(master=frm_entry, text="\n{Inches}")

ent_inches.grid(row=0, column=0, sticky="e")

lbl_inches.grid(row=0, column=1, sticky="w")

# Create the conversion Button and result display Label

btn_convert = tk.Button(master=window,text="-->",command=inches_to_cm)

lbl_result = tk.Label(master=window, text="\n{CM}")

# Set-up the layout using the .grid() geometry manager

frm_entry.grid(row=0, column=0, padx=10)

btn_convert.grid(row=0, column=1, pady=10)

lbl_result.grid(row=0, column=2, padx=10)

# Run the application

window.mainloop()