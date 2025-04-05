from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

windows = Tk()
windows.title(" Codingal's Text Editor")
windows.geometry("600x400")
windows.rowconfigure(0, minsize=800, weight=1)
windows.columnconfigure(1, minsize=800, weight=1)

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All ""Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(1.0, text)
        input_file.close()
    windows.title(f"Codingal's Text Editor - {filepath}")
def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    windows.title(f"Codingal's Text Editor - {filepath}")

txt_edit = Text(windows)
fr_button = Frame(windows, relief=FLAT, bd=2)
btn_open = Button(fr_button, text="Open",
command=open_file)
btn_save = Button(fr_button, text="Save As....",
command=save_file)


btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=0, column=1, sticky="ew", padx=5)

fr_button.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=1, column=0, sticky="nsew")

windows.mainloop()
    