from tkinter import *
import tkinter


class SoNguyen():
    def __init__(self, a):
        self.a = a
        return

    def SNT(self):
        check = 1
        for i in range(2, self.a):
            if self.a % i == 0:
                check = 0
                break
            else:
                check = 1
        return check

    def SoDoiXung(self):
        temp = self.a
        sdx = 0
        while temp != 0:
            sdx = sdx * 10 + temp % 10
            temp = temp // 10
        if sdx == self.a:
            return True
        else:
            return False


def checkSNT():
    entry = int(text1.get())
    sn = SoNguyen(entry)
    if sn.SNT() == 1:
        lb4 = Label(win, text="La so nguyen to").place(x=100, y=250)
    else:
        lb3 = Label(win, width=80).place(x=100, y=250)
        lb4 = Label(win, text="Kp la so nguyen to").place(x=100, y=250)


def checkSDX():
    entry = int(text1.get())
    sdx = SoNguyen(entry)
    if sdx.SoDoiXung():
        lb4 = Label(win, text="La so doi xung").place(x=100, y=300)
    else:
        lb4 = Label(win, text="Kp la so doi xung").place(
            x=100, y=300)


win = Tk()
win.title("Bai 6")
win.geometry("400x500")

global text1
text1 = StringVar()


lb1 = Label(win, text="Nhap so: ").place(x=50, y=50)
entry1 = Entry(win, textvariable=text1).place(x=150, y=50)

btn = Button(win, text="checkSNT", command=checkSNT).place(x=50, y=100)
btn1 = Button(win, text="checkSDX", command=checkSDX).place(x=50, y=150)
win.mainloop()
