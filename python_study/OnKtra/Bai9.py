
import math
from tkinter import *


class Diem():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        return


def KhoangCach():
    try:
        diem1 = Diem(float(text1.get()), float(text2.get()))
        diem2 = Diem(float(text3.get()), float(text4.get()))
        lb3 = Label(win, width=40).place(x=100, y=250)

        lb4 = Label(win, text="Khoang cach: " + str(math.sqrt((diem1.x -
                    diem2.x)**2 + (diem1.y - diem2.y)**2))).place(x=100, y=250)
    except:
        lb4 = Label(win, text="Nhap sai").place(x=100, y=250)


win = Tk()
win.title("Bai 3")
win.geometry("400x500")

text1 = StringVar()
text2 = StringVar()
text3 = StringVar()
text4 = StringVar()

l1 = Label(win, text="Nhap toa do diem a:").place(x=50, y=50)
l2 = Label(win, text="x1").place(x=50, y=70)
entry1 = Entry(win, textvariable=text1).place(x=100, y=70)
l3 = Label(win, text="y1").place(x=230, y=70)
entry2 = Entry(win, textvariable=text2).place(x=250, y=70)

l4 = Label(win, text="Nhap toa do diem b:").place(x=50, y=100)
l5 = Label(win, text="x2").place(x=50, y=130)
entry2 = Entry(win, textvariable=text3).place(x=100, y=130)
l6 = Label(win, text="y2").place(x=230, y=130)
entry2 = Entry(win, textvariable=text4).place(x=250, y=130)

btn = Button(win, text="Khoang cach", command=KhoangCach).place(x=100, y=200)

win.mainloop()
