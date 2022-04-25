import tkinter as tk


def Check():
    n = int(text1.get())
    s = 0
    for i in range(1, n+1):
        s += 1/i
    l1 = tk.Label(window, text="Tong la: " + str(s)).place(x=20, y=100)
    return


window = tk.Tk()
window.title("Tinh")
window.geometry('400x300')
text1 = tk.StringVar()
l1 = tk.Label(window, text="Nhap so: ").place(x=20, y=20)
t1 = tk.Entry(window, textvariable=text1).place(x=100, y=20)
b1 = tk.Button(window, text="Check", command=Check).place(x=100, y=60)
window.mainloop()
