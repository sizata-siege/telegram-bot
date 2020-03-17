from tkinter import *

window = Tk()

def s():
    miles = float(e1_value.get()) * 1.6
    t1.insert(END, miles)

b1 = Button(window, text = "Convert to miles", command = s)
b1.grid(row = 0, column = 0, rowspan = 3)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 3)

t1 = Text(window, height = 1, width = 20)
t1.grid(row = 0, column = 4)

window.mainloop()