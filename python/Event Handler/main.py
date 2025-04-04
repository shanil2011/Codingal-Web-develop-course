from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def handle_keypress(event):
    """"Print the character associated to the key pressed."""
    print({event.char})

window.bind("<KeyPress>", handle_keypress)

def handle_click(event):
    print("\n The button was clicked")

button = Button(text = "Click me")
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()