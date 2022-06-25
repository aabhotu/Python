import math


class dientro():
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def giatri(self):
        gt = (int(self.v1)*10+int(self.v2))*math.pow(10, int(self.v3))
        return gt


L = []
for i in range(3):
    print("Nhap cac vong mau cua dien tro thu %d " % (i+1))
    v1 = str(input("Nhap mau cua vong 1: "))
    if v1 == "nau":
        v1 = "0"
    if v1 == "den":
        v1 = "1"
    if v1 == "do":
        v1 = "2"
    if v1 == "cam":
        v1 = "3"
    if v1 == "vang":
        v1 = "4"
    if v1 == "luc":
        v1 = "5"
    if v1 == "lam":
        v1 = "6"
    if v1 == "tim":
        v1 = "7"
    if v1 == "xam":
        v1 = "8"
    if v1 == "trang":
        v1 = "9"
    v2 = str(input("Nhap mau cua vong 2: "))
    if v2 == "nau":
        v2 = "0"
    if v2 == "den":
        v2 = "1"
    if v2 == "do":
        v2 = "2"
    if v2 == "cam":
        v2 = "3"
    if v2 == "vang":
        v2 = "4"
    if v2 == "luc":
        v2 = "5"
    if v2 == "lam":
        v2 = "6"
    if v2 == "tim":
        v2 = "7"
    if v2 == "xam":
        v2 = "8"
    if v2 == "trang":
        v1 = "9"
    v3 = str(input("Nhap mau cua vong 3: "))
    if v3 == "nau":
        v3 = "0"
    if v3 == "den":
        v3 = "1"
    if v3 == "do":
        v3 = "2"
    if v3 == "cam":
        v3 = "3"
    if v3 == "vang":
        v3 = "4"
    if v3 == "luc":
        v3 = "5"
    if v3 == "lam":
        v3 = "6"
    if v3 == "tim":
        v3 = "7"
    if v3 == "xam":
        v3 = "8"
    if v3 == "trang":
        v3 = "9"
    L.append(dientro(v1, v2, v3))

myList = []
Min = L[0].giatri()
for i in range(3):
    print("Gia tri cua dien tri %d" % (i+1) + str(L[i].giatri()))
    myList.append(L[i].giatri())
    if Min > L[i].giatri():
        Min = L[i].giatri()
        dem = i

B = tuple(myList)
