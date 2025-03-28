from tkinter import *
from datetime import date

root = Tk()
root.title("Not a window")
root.geometry("400x300")

lbl = Label(text="Hello World" , fg="white", bg="black", height=1, width=200)

name_lbl = Label(text="Full name", bg="#3895D3")
name_entry = Entry()

def display():
    name = name_entry.get()
    
    global message
    message = "Welcome to the Application! \nToday's date is: "
    greet = "Hello "+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
    

text_box = Text(height=3)

btn = Button(text="begin", command=display, height=1, bg="yellow", fg="black")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()


root.mainloop()