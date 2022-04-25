import tkinter as tk


def ThucHien():
    a = int(text1.get())
    b = int(text2.get())
    tong = a + b
    l3 = tk.Label(cs, text="Tong cua 2 so = " + str(tong)).place(x=20, y=100)
    return


cs = tk.Tk()
cs.title("Cua so chinh")
cs.geometry('400x300')
text1 = tk.StringVar()
text2 = tk.StringVar()
l1 = tk.Label(cs, text='Hay nhap a:'). place(x=20, y=20)
t1 = tk.Entry(cs, textvariable=text1).place(x=100, y=20)

l2 = tk.Label(cs, text='Hay nhap b:'). place(x=10, y=40)
t2 = tk.Entry(cs, textvariable=text2).place(x=100, y=40)
b1 = tk.Button(cs, text='tinh toan', command=ThucHien).place(x=100, y=60)
cs.mainloop()
