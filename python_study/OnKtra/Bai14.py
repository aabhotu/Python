from tkinter import *
import math


class SoNguyen():
    def __init__(self, a):
        self.a = a

    def SDX(self):
        temp = self.a
        snd = 0
        while temp > 0:
            snd = snd*10 + temp % 10
            temp //= 10
        if snd == self.a:
            return True
        else:
            return False

    def SHT(self):
        tong = 0
        for i in range(1, self.a):
            if self.a % i == 0:
                tong += i
        if tong == self.a:
            return True
        else:
            return False


myList = []
for i in range(3):
    print("Nhap so nguyen %d" % i)
    so = int(input())
    myList.append(so)

for i in range(3):
    so = SoNguyen(myList[i])
    if so.SHT():
        print(myList[i])
