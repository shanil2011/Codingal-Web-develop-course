from tkinter import *

window = Tk()
window.title("Tkinter sample window")
window.geometry("300x300")

greeting = Label(text="Hello User!", fg='white', bg='red')

button = Button(text="Click me!", fg='white', bg='green')

entry = Entry(fg='white', bg='blue', width=30)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text='Sample Frame')
label.pack()

textbox = Text(fg='green', bg='yellow')
textbox.pack()

window.mainloop()