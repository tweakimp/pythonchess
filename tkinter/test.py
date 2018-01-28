from random import randint
from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=200)
canvas.pack()


def click(event):
    if canvas.find_withtag(CURRENT):
        canvas.itemconfig(CURRENT, fill="blue")
        canvas.update_idletasks()
        canvas.after(200)
        canvas.itemconfig(CURRENT, fill="red")


for i in range(100):
    x, y = randint(0, 200 - 1), randint(0, 200 - 1)
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")

canvas.bind("<Button-1>", click)

root.mainloop()
