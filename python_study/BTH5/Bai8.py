from tkinter import *


class soThuc():
    def __init__(self, a):
        self.a = a
        return

    def CheckAm(self):
        if self.a < 0:
            return True
        else:
            return False

    def CheckDuong(self):
        if self.a > 0:
            return True
        else:
            return False

    def Dem(self):
        b = list(self.a)
        b.reverse()
        dem = 0
        for i in range(len(b)):
            if b[i] == '.':
                break
            else:
                dem += 1
        return dem


def KtraAm():
    entry = float(text1.get())
    st = soThuc(entry)
    if st.CheckAm():
        lb1 = Label(win, text="Dung").place(x=50, y=130)
    else:
        lb1 = Label(win, text="Sai").place(x=50, y=130)
    lb3 = Label(win, text="So chu so sau dau phay: " +
                str(st.Dem())).place(x=50, y=250)


def KtraDuong():
    entry = float(text1.get())
    st = soThuc(entry)
    if st.CheckDuong():
        lb2 = Label(win, text="Dung").place(x=50, y=200)
    else:
        lb2 = Label(win, text="Sai").place(x=50, y=200)


win = Tk()
win.title("Bai 8")
win.geometry("500x400")

text1 = StringVar()
l1 = Label(win, text="Nhap so a: ").place(x=50, y=50)
e1 = Entry(win, textvariable=text1).place(x=150, y=50)

bt1 = Button(win, text="Ktra so am", command=KtraAm).place(x=50, y=100)
bt2 = Button(win, text="Ktra so duong", command=KtraDuong).place(x=50, y=170)

win.mainloop()
