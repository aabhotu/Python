import tkinter as tk


def Check():
    a = int(text1.get())
    if a % 2 == 0:
        l3 = tk.Label(window, text="So chan").place(x=20, y=100)
    else:
        l3 = tk.Label(window, text="So le").place(x=20, y=100)
    return


window = tk.Tk()
window.title("Cua so chinh")
window.geometry('400x300')
text1 = tk.StringVar()
l1 = tk.Label(window, text="Nhap so: ").place(x=20, y=20)
t1 = tk.Entry(window, textvariable=text1).place(x=100, y=20)
b1 = tk.Button(window, text="Check", command=Check).place(x=100, y=60)
window.mainloop()
