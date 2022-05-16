from tkinter import*
import math


def luachon(event):
    index1 = list1.curselection()
    label1.config(text=" Ban chon phep tinh " + str(list1.get(index1)))
    label1.place(x=100, y=240)
    return


def tinhtoan():
    a = int(text1.get())
    b = int(text2.get())
    index1 = list1.curselection()
    if str(list1.get(index1)) == "cong":
        l3 = Label(cs, width=40).place(x=100, y=300)
        l4 = Label(cs, text="tong la:"+str(a+b)).place(x=100, y=300)
    if str(list1.get(index1)) == "tru":
        l3 = Label(cs, width=40).place(x=100, y=300)
        l4 = Label(cs, text="hieu la:"+str(a-b)).place(x=100, y=300)
    if str(list1.get(index1)) == "nhan":
        l3 = Label(cs, width=40).place(x=100, y=300)
        l4 = Label(cs, text="tich la:"+str(a*b)).place(x=100, y=300)
    if str(list1.get(index1)) == "chia":
        if b != 0:
            l3 = Label(cs, width=40).place(x=100, y=300)
            l4 = Label(cs, text="thuong la:"+str(a/b)).place(x=100, y=300)
        elif b == 0:
            l3 = Label(cs, width=40).place(x=100, y=300)
            l4 = Label(cs, text="Khong the thuc hien phep tinh").place(
                x=100, y=300)
    if str(list1.get(index1)) == "can bac 2":
        if a >= 0:
            l3 = Label(cs, width=40).place(x=100, y=300)
            l4 = Label(cs, text="can bac 2 la:" +
                       str(math.sqrt(a))).place(x=100, y=300)
        if a < 0:
            l3 = Label(cs, width=40).place(x=100, y=300)
            l4 = Label(cs, text="Khong the thuc hien phep tinh").place(
                x=100, y=300)
    return


cs = Tk()
cs.title("Tinh toan")
cs.geometry('600x500')
ds = ["cong", "tru", "nhan", "chia", "can bac 2"]
text1 = StringVar()
text2 = StringVar()
l0 = Label(cs, text="Hay nhap 2 so").place(x=10, y=20)
l1 = Label(cs, text=" a ").place(x=10, y=50)
t1 = Entry(cs, textvariable=text1).place(x=30, y=50)
l2 = Label(cs, text=" b ").place(x=160, y=50)
t2 = Entry(cs, textvariable=text2).place(x=180, y=50)
list1 = Listbox(cs)
for i in range(0, len(ds)):
    list1.insert(i, ds[i])
list1.place(x=100, y=80)
list1.bind('<<ListboxSelect>>', luachon)
label1 = Label(cs)
b1 = Button(cs, text="Tinh Toan", command=tinhtoan).place(x=100, y=280)
b2 = Button(cs, text="Dong", command=cs.quit()).place(x=100, y=320)
cs.mainloop()
