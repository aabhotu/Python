from tkinter import *
from tkinter import ttk
import math

win = Tk()
win.title("Bai 1")
win.geometry("400x500")


def GiaiPTB1():
    a = int(text1.get())
    b = int(text2.get())
    if a == 0:
        if b == 0:
            lb4 = Label(win, text="Phuong trinh vo so nghiem").place(
                x=100, y=300)
        else:
            # lb4.config(text=" ").place(x=100, y=300)
            lb4 = Label(win, text="Phuong trinh vo nghiem").place(x=100, y=300)
    else:
        x = -b/a
        lb4 = Label(win, text="Pt cos nghiem: " + str(x)).place(x=100, y=300)
    return


def GiaiPTB2():
    a = int(text1.get())
    b = int(text2.get())
    c = int(text3.get())
    if a == 0:
        if b == 0:
            # lb4.config(text=" ").place(x=100, y=300)
            lb4 = Label(win, text="Phuong trinh vo nghiem").place(
                x=100, y=350)
        else:
            # lb4.config(text=" ").place(x=100, y=300)
            lb4 = Label(win, text="Phuong trinh co 1 nghiem x = " +
                        str(-c/b)).place(x=100, y=350)
    else:
        # lb4.config(text=" ").place(x=100, y=300)
        delta = (b*b-4*a*c)/2
        if delta < 0:
            lb4 = Label(win, text="Phuong trinh vo nghiem").place(
                x=100, y=350)
        elif delta == 0:
            x = -b/2/a
            lb4 = Label(win, text="Phuong trinh co nghiem kep x = " +
                        str(-b/(2*a))).place(x=100, y=350)
        else:
            x1 = round((-b+math.sqrt(delta))/2/a, 3)
            x2 = round((-b-math.sqrt(delta))/2/a, 3)
            lb4 = Label(win, text="Phuong trinh co 2 nghiem phan biet x = " +
                        str(x1) + " va " + str(x2)).place(x=100, y=350)
    return


text1 = StringVar()
text2 = StringVar()
text3 = StringVar()

lb1 = Label(text="Nhap a: ").place(x=50, y=100)
lb2 = Label(text="Nhap b: ").place(x=50, y=130)
lb3 = Label(text="Nhap c: ").place(x=50, y=160)
txt1 = Entry(win, textvariable=text1).place(x=100, y=100)
txt2 = Entry(win, textvariable=text2).place(x=100, y=130)
txt3 = Entry(win, textvariable=text3).place(x=100, y=160)

var = IntVar()
btn1 = Radiobutton(win, text="GiaiPTB1", command=GiaiPTB1, variable=var,
                   value=1).place(x=100, y=200)
btn2 = Radiobutton(win, text="GiaiPTB2", command=GiaiPTB2, variable=var,
                   value=2).place(x=100, y=230)

lb4 = Label(text=" ")


def handleSubmit():
    if var.get() == 1:
        GiaiPTB1()
    else:
        GiaiPTB2()
    return


btn = Button(text="check", command=handleSubmit).place(x=100, y=270)

win.mainloop()
