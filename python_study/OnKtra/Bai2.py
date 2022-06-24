from tkinter import *
import math


class HCN:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ChuVi(self):
        return (self.a+self.b)*2

    def DienTich(self):
        return self.a*self.b

    def DuongCheo(self):
        return round(math.sqrt(self.a**2+self.b**2))


def HCN1():
    en1 = float(text1.get())
    en2 = float(text2.get())
    global hcn1
    hcn1 = HCN(en1, en2)
    t1 = Label(win, text="Chu vi 1: " + str(hcn1.ChuVi()) + "\nDien tich 1: " +
               str(hcn1.DienTich()) + "\nDuong cheo 1: " + str(hcn1.DuongCheo())).place(x=50, y=200)


def HCN2():
    en1 = float(text3.get())
    en2 = float(text4.get())
    global hcn2
    hcn2 = HCN(en1, en2)
    t1 = Label(win, text="Chu vi 2: " + str(hcn2.ChuVi()) + "\nDien tich 2: " +
               str(hcn2.DienTich()) + "\nDuong cheo 2: " + str(hcn2.DuongCheo())).place(x=250, y=200)


def HCN3():
    en1 = float(text5.get())
    en2 = float(text6.get())
    global hcn3
    hcn3 = HCN(en1, en2)
    t1 = Label(win, text="Chu vi 3: " + str(hcn3.ChuVi()) + "\nDien tich 3: " +
               str(hcn3.DienTich()) + "\nDuong cheo 3: " + str(hcn3.DuongCheo())).place(x=450, y=200)


def TimMax():
    if(hcn1.ChuVi() > hcn2.ChuVi() and hcn1.ChuVi() > hcn3.ChuVi()):
        ChuViMax = hcn1.ChuVi()
    elif (hcn2.ChuVi() > hcn3.ChuVi()):
        ChuViMax = hcn2.ChuVi()
    else:
        ChuViMax = hcn3.ChuVi()
    l1 = Label(win,  text="Chu vi max: " + str(ChuViMax)).place(x=200, y=450)


win = Tk()
win.title("Bai2")
win.geometry("1200x500")

global text1
global text2
global text3
global text4
global text5
global text6

text1 = StringVar()
text2 = StringVar()
text3 = StringVar()
text4 = StringVar()
text5 = StringVar()
text6 = StringVar()

l1 = Label(win, text="Tu giac 1: ").place(x=30, y=30)
l2 = Label(win, text="Nhap canh a: ").place(x=50, y=50)
en1 = Entry(win, textvariable=text1).place(x=140, y=50)

l3 = Label(win, text="Nhap canh b: ").place(x=50, y=80)
en2 = Entry(win, textvariable=text2).place(x=140, y=80)

btn1 = Button(win, text="HCN1", command=HCN1).place(x=50, y=110)

#!hcn2
l4 = Label(win, text="Tu giac 1: ").place(x=250, y=30)
l5 = Label(win, text="Nhap canh a: ").place(x=250, y=50)
en3 = Entry(win, textvariable=text3).place(x=340, y=50)

l6 = Label(win, text="Nhap canh b: ").place(x=250, y=80)
en4 = Entry(win, textvariable=text4).place(x=350, y=80)

btn2 = Button(win, text="HCN2", command=HCN2).place(x=250, y=110)

#!hcn3
l7 = Label(win, text="Tu giac 1: ").place(x=450, y=30)
l8 = Label(win, text="Nhap canh a: ").place(x=450, y=50)
en5 = Entry(win, textvariable=text5).place(x=540, y=50)

l9 = Label(win, text="Nhap canh b: ").place(x=450, y=80)
en6 = Entry(win, textvariable=text6).place(x=550, y=80)

btn3 = Button(win, text="HCN2", command=HCN3).place(x=450, y=110)

btn4 = Button(win, text="Chu Vi max: ", command=TimMax).place(x=100, y=450)

win.mainloop()
