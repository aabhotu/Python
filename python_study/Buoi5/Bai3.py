import tkinter as tk


def func():
    n = str(text1.get())
    chuoi = n.split(',')
    n = ' '.join(chuoi)

    chuoi = n.split('.')
    n = ' '.join(chuoi)

    chuoi = n.split(' ')
    chuoi2 = []
    for i in range(len(chuoi)):
        if chuoi[i] == '':
            continue
        else:
            chuoi2.append(chuoi[i])
    l3 = tk.Label(window, text=chuoi2).place(x=20, y=100)
    l4 = tk.Label(window, text="Chieu dai cua chuoi: " +
                  str(len(chuoi2))).place(x=20, y=120)

    for i in range(len(chuoi2)):
        chuoi2[i] = str(chuoi2[i]).capitalize()
    n = ' '.join(chuoi2)
    l5 = tk.Label(window, text="Chuoi sau khi chuan hoa: " +
                  n).place(x=20, y=140)


window = tk.Tk()
window.title("Xu ly chuoi")
window.geometry('400x300')
text1 = tk.StringVar()
l0 = tk.Label(window, text="Nhap chuoi: ").place(x=20, y=20)
t0 = tk.Entry(window, textvariable=text1).place(x=100, y=20)

b1 = tk.Button(window, text="Check", command=func).place(x=100, y=80)
window.mainloop()
