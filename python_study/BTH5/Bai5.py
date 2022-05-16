from tkinter import *
import math


class TamGiac():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class TamGiacDeu(TamGiac):
    def ChuVi(self):
        return self.a + self.b + self.c

    def DienTich(self):
        return self.a ** 2 * (math.sqrt(3)/4)


class TamGiacVuong(TamGiac):
    def ChuVi(self):
        return self.a + self.b + self.c

    def DienTich(self):
        return (self.a * self.b)/2


def TinhTGD():
    try:
        entry = float(text.get())
        tgd = TamGiacDeu(entry, entry, entry)
        lb4 = Label(win, text="Chu vi: "+str(tgd.ChuVi()) +
                    "\nDien tich: "+str(tgd.DienTich())).place(x=100, y=300)
    except:
        lb4 = Label(win, text="Nhap sai").place(x=100, y=300)


def TGD_Widget():
    global text
    text = StringVar()
    l = Label(win, text="Nhap canh tg: ").place(x=20, y=200)
    entry = Entry(win, textvariable=text).place(x=100, y=200)
    btn = Button(win, text="Tinh", command=TinhTGD).place(x=100, y=250)


def TinhTGV():
    try:
        entry1 = float(text1.get())
        entry2 = float(text2.get())
        entry3 = math.sqrt(entry1**2+entry2**2)

        tgv = TamGiacVuong(entry1, entry2, entry3)
        lb5 = Label(win, text="Chu vi: "+str(tgv.ChuVi()) +
                    "\nDien tich: "+str(tgv.DienTich())).place(x=100, y=450)
    except:
        lb5 = Label(win, text="Nhap sai").place(x=100, y=450)


def TGV_Widget():
    global text1
    global text2
    global text3

    text1 = StringVar()
    text2 = StringVar()
    # text3 = StringVar()

    l1 = Label(win, text="Nhap canh a: ").place(x=20, y=350)
    l2 = Label(win, text="Nhap canh b: ").place(x=20, y=375)
    # l3 = Label(win, text="Nhap canh a: ").place(x=20, y=400)
    entry1 = Entry(win, textvariable=text1).place(x=100, y=350)
    entry2 = Entry(win, textvariable=text2).place(x=100, y=375)
    # entry3 = Entry(win, textvariable=text3).place(x=100, y=400)

    btn = Button(win, text="Tinh", command=TinhTGV).place(x=100, y=425)


win = Tk()
win.title("Bai 5")
win.geometry("400x700")


btn1 = Button(win, text="Tam giac deu", command=TGD_Widget).place(x=100, y=100)
btn2 = Button(win, text="Tam giac vuong",
              command=TGV_Widget).place(x=100, y=150)
win.mainloop()
