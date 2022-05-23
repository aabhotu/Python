from tkinter import *

myList = []
n = int(input("Nhap so phan tu: "))
for i in range(n):
    myList.append(int(input("Nhap phan tu thu %d: " % (i+1))))

myDict = {}
for i in range(len(myList)):
    myDict[i] = myList[i]**3

win = Tk()
win.title("Bai 7")
win.geometry("400x500")


b1 = Button(win, text="close", command=win.destroy).place(x=50, y=200)
list1 = Listbox(win, width=20, height=10)
for i in range(n):
    a = str(i) + ' : ' + str(myDict[i])
    list1.insert(i, a)
list1.pack()

win.mainloop()
