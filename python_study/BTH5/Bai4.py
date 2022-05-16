import math
from tkinter import *


def Choose(event):
    index1 = list1.curselection()
    label1.config(text="Ban chon phep tinh: "+str(list1.get(index1)))
    label1.place(x=100, y=250)
    return


def TinhToan():
    n = int(text.get())
    index1 = list1.curselection()
    if str(list1.get(index1)) == "Tong":
        tong = 0
        for i in range(1, n+1):
            tong += i
        l3 = Label(win, width=40).place(x=100, y=350)
        lb2 = Label(win, text="Tong la: " + str(tong)).place(x=100, y=350)
    if str(list1.get(index1)) == "Tich":
        tich = 1
        for i in range(1, n+1):
            tich *= i
        l3 = Label(win, width=40).place(x=100, y=350)
        lb2 = Label(win, text="Tich la: " + str(tich)).place(x=100, y=350)
    if str(list1.get(index1)) == "Hieu":
        hieu = 1
        for i in range(1, n+1):
            hieu -= 1/i
        l3 = Label(win, width=40).place(x=100, y=350)
        lb2 = Label(win, text="Hieu la: " + str(hieu)).place(x=100, y=350)
    if str(list1.get(index1)) == "Thuong":
        thuong = 1
        for i in range(1, n+1):
            thuong *= 1/i
        l3 = Label(win, width=40).place(x=100, y=350)
        lb2 = Label(win, text="Thuong la: " + str(thuong)).place(x=100, y=350)
    if str(list1.get(index1)) == "Mu":
        mu = 0
        for i in range(1, n+1):
            mu += i**2
        l3 = Label(win, width=40).place(x=100, y=350)
        lb2 = Label(win, text="Mu la: " + str(mu)).place(x=100, y=350)


win = Tk()
win.title("Bai 4")
win.geometry("400x500")
ds = ["Tong", "Hieu", "Tich", "Thuong", "Mu"]

text = StringVar()

lb1 = Label(win, text="Hay nhap 1 so: ").place(x=50, y=50)
entry1 = Entry(win, textvariable=text).place(x=150, y=50)

list1 = Listbox(win)
for i in range(len(ds)):
    list1.insert(i, ds[i])

list1.place(x=100, y=100)
list1.bind("<<ListboxSelect>>", Choose)
label1 = Label(win)
btn1 = Button(win, text="tinh toan", command=TinhToan).place(x=100, y=300)
win.mainloop()
