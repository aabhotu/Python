import tkinter as tk
import math


def GiaiPT():
    a = int(text1.get())
    b = int(text2.get())
    c = int(text3.get())
    if a == 0:
        if b == 0:
            l4 = tk.Label(window, width=80).place(x=20, y=100)
            l3 = tk.Label(window, text="Phuong trinh vo nghiem").place(
                x=20, y=100)
        else:
            l4 = tk.Label(window, width=80).place(x=20, y=100)
            l3 = tk.Label(
                window, text="Phuong trinh co 1 nghiem x = " + str(-c/b)).place(x=20, y=100)
    else:
        delta = (b*b-4*a*c)/2
        if delta < 0:
            # l3.config(text="").config(
            #     text="Phuong trinh vo nghiem").place(x=20, y=100)
            l4 = tk.Label(window, width=80).place(x=20, y=100)
            l3 = tk.Label(window, text="Phuong trinh vo nghiem").place(
                x=20, y=100)
        elif delta == 0:
            x = -b/2/a
            l4 = tk.Label(window, width=80).place(x=20, y=100)
            l3 = tk.Label(window, text="Phuong trinh co nghiem kep x = " +
                          str(-b/(2*a))).place(x=20, y=100)
        else:
            x1 = round((-b+math.sqrt(delta))/2/a, 3)
            x2 = round((-b-math.sqrt(delta))/2/a, 3)
            l4 = tk.Label(window, width=80).place(x=20, y=100)
            l3 = tk.Label(window, text="Phuong trinh co 2 nghiem phan biet x = " +
                          str(x1) + " va " + str(x2)).place(x=20, y=100)
    return


window = tk.Tk()
window.title("Giai phuong trinh bac 2")
window.geometry('400x300')
text1 = tk.StringVar()
text2 = tk.StringVar()
text3 = tk.StringVar()


l0 = tk.Label(window, text="Nhap so a: ").place(x=20, y=20)
t0 = tk.Entry(window, textvariable=text1).place(x=100, y=20)

l1 = tk.Label(window, text="Nhap so b: ").place(x=20, y=40)
t1 = tk.Entry(window, textvariable=text2).place(x=100, y=40)

l2 = tk.Label(window, text="Nhap so c: ").place(x=20, y=60)
t2 = tk.Entry(window, textvariable=text3).place(x=100, y=60)

b1 = tk.Button(window, text="Check", command=GiaiPT).place(x=100, y=80)

l3 = tk.Label(window, text=" ")
window.mainloop()
