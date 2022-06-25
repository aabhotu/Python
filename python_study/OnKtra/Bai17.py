import math


class PTB2():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Nghiem(self):
        global myTuple
        myTuple = []
        if self.a == 0:
            if self.b == 0:
                print("PTVN")
            else:
                x = -c/b
                myTuple.append(x)
                print("pt co 1n: " + str(x))
        else:
            delta = self.b*self.b-4*self.a*self.c
            if delta == 0:
                x = -self.b/(2*self.a)
                print("Pt co nghiem kep x = " + str(x))
                myTuple.append(x)
            elif delta < 0:
                print("PTVN")
            else:
                x1 = (-self.b + math.sqrt(delta))/(2*self.a)
                x2 = (-self.b - math.sqrt(delta))/(2*self.a)
                myTuple.append(x1)
                myTuple.append(x2)
                print("PT co 2 nghiem pb x1 = " + str(x1) +
                      "x2 = " + str(x2))
        # myTuple = tuple(myTuple)
        # print(myTuple)


myList = []
tupleNghiem = []
for i in range(2):
    print("Nhap pht %d" % i)
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    c = int(input("Nhap c: "))
    obj = PTB2(a, b, c)
    myList.append(obj)
for i in range(2):
    myList[i].Nghiem()
    print(myTuple)
    tupleNghiem += myTuple

tupleNghiem = tuple(tupleNghiem)
print(max(tupleNghiem))
