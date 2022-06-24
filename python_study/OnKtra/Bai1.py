from tkinter import *


class HTG():
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def ChuVi(self):
        return self.a+self.b+self.c+self.d

    def TimMax(self):
        if (self.a > self.b and self.a > self.c and self.a > self.d):
            canhMax = self.a
        elif (self.b > self.c and self.b > self.d):
            canhMax = self.b
        elif (self.c > self.d):
            canhMax = self.c
        else:
            canhMax = self.d
        return canhMax


def TG1():
    en1 = float(text1.get())
    en2 = float(text2.get())
    en3 = float(text3.get())
    en4 = float(text4.get())
    tg1 = HTG(en1, en2, en3, en4)
    l1 = Label(win, text="Chu vi1: " + str(tg1.ChuVi()) +
               "Canh max: " + str(tg1.TimMax())).place(x=50, y=200)


win = Tk()
win.title("Bai1")
win.geometry("1000x500")

global text1
global text2
global text3
global text4

text1 = StringVar()
text2 = StringVar()
text3 = StringVar()
text4 = StringVar()

tg1 = Label(win, text="Tu giac 1: ").place(x=20, y=30)
l1 = Label(win, text="Nhap canh a: ").place(x=50, y=50)
en1 = Entry(win, textvariable=text1).place(x=130, y=50)
l2 = Label(win, text="Nhap canh b: ").place(x=50, y=80)
en2 = Entry(win, textvariable=text2).place(x=130, y=80)
l3 = Label(win, text="Nhap canh c: ").place(x=50, y=110)
en3 = Entry(win, textvariable=text3).place(x=130, y=110)
l4 = Label(win, text="Nhap canh d: ").place(x=50, y=140)
en4 = Entry(win, textvariable=text4).place(x=130, y=140)
btn1 = Button(win, text="Tu giac 1", command=TG1).place(x=50, y=180)

win.mainloop()
