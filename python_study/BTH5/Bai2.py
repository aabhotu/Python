from tkinter import *
from tkinter import ttk
import math


class HinhTuGiac():
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        return


class HCN(HinhTuGiac):

    def ChuVi(self):
        return (self.a + self.b) * 2

    def DienTich(self):
        return self.a * self.b


class HV(HCN):
    def ChuVi(self):
        return self.a * 2

    def DienTich(self):
        return self.a**2


def TinhHCN():
    try:
        entry1 = float(text1.get())
        entry2 = float(text2.get())
        hcn = HCN(entry1, entry2, entry1, entry2)
        lb4 = Label(win, text="Chu vi: " +
                    str(hcn.ChuVi()) + "\nDien tich: " + str(hcn.DienTich())).place(x=100, y=250)
    except:
        lb4 = Label(win, text="Nhap sai").place(x=100, y=250)


def TinhHV():
    try:
        entry = float(text.get())
        hv = HV(entry, entry, entry, entry)
        lb4 = Label(win, text="Chu vi: " + str(hv.ChuVi()) +
                    "\nDien tich: " + str(hv.DienTich())).place(x=100, y=250)
    except:
        lb4 = Label(win, text="Nhap sai").place(x=100, y=250)


win = Tk()
win.title("Bai 2")
win.geometry("400x500")


def HcnWidget():
    global text1
    global text2

    text1 = StringVar()
    text2 = StringVar()

    for widget in win.winfo_children():
        widget.destroy()

    l1 = Label(win, text="Nhap canh a: ").place(x=50, y=100)
    l2 = Label(win, text="Nhap canh b: ").place(x=50, y=150)

    box1 = Entry(win, textvariable=text1).place(x=150, y=100)
    box2 = Entry(win, textvariable=text2).place(x=150, y=150)

    b3 = Button(win, text="Tinh: ",
                command=TinhHCN).place(x=150, y=200)
    b5 = Button(win, text="Close", command=win.destroy).place(x=150, y=300)


def HvWidget():
    global text
    text = StringVar()
    for widget in win.winfo_children():
        widget.destroy()
    l1 = Label(win, text="Nhap canh a: ").place(x=50, y=100)

    box1 = Entry(win, textvariable=text).place(x=150, y=100)

    b3 = Button(win, text="Tinh: ", command=TinhHV).place(x=150, y=200)


bt1 = Button(win, text="HCN", command=HcnWidget).place(x=150, y=50)
bt2 = Button(win, text="HV", command=HvWidget).place(x=150, y=100)
win.mainloop()
