from tkinter import *
import tkinter


class HinhTron():
    def __init__(self, bk):
        self.bk = bk
        return

    def ChuVi(self):
        return 3.14*self.bk*2

    def DienTich(self):
        return 3.14*self.bk*self.bk


def Tinh():
    try:
        entry = float(text1.get())
        htron = HinhTron(entry)
        lb1 = Label(win, text="Chu vi: " + str(htron.ChuVi()) +
                    "\nDien tich: " + str(htron.DienTich())).place(x=50, y=100)
    except:
        lb1 = Label(win, text="Nhap sai").place(x=50, y=100)


win = Tk()
win.title("Bai 8")
win.geometry("500x400")

text1 = StringVar()
w = Label(win, text='Nhap ban kinh: ').place(x=50, y=50)
e = Entry(win, textvariable=text1).place(x=150, y=50)
b1 = Button(win, text="Tinh toan", command=Tinh). place(x=50, y=150)

win.mainloop()
