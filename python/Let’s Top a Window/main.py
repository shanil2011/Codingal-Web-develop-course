from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("top")
    
    l2 = Label(top, text="This is  top level window")
    l2.pack()

l = Label(root, text="This is root window")
btn = Button(root, text="Click here to open another Window", command=topwin)

l.pack()
btn.pack()
