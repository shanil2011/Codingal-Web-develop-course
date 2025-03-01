from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Demination Calculator")
root.configure(bg="light blue")
root.geometry("650x400")

label1 = Label(root, text="Hey User! Welcome to Denomination Counter Application.", bg="light blue", )
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    Msgbox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if Msgbox == "ok":
        topwin()

button1 = Button(root,
                 text="Lets get started", 
                 command=msg,
                 bg="light green",
                 fg="White")

button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")
    

    label = Label(top, text="Enter total amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey')

    l1 = Label(top, text="1000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note1000 = amount // 1000
            amount %= 1000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            amount %= 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note1000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

    btn = Button(top, text="Calculate", command=calculator, bg='grey', fg='white')

    label.place(x=230, y=50   )
    entry.place(x=200, y=80  )
    btn.place(x=240, y=120   )
    lbl.place(x=140, y=170   )

    l1.place(x=180, y=200   )
    l2.place(x=180, y=230   )
    l3.place(x=180, y=260   )

    t1.place(x=270, y=200   )
    t2.place(x=270, y=230   )
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()

