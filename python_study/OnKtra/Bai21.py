class LuyThua:
    def __init__(self, a):
        self.a = a

    def BinhPhuong(self):
        return self.a**2

    def LapPhuong(self):
        return self.a**3

    def GiaiThua(self):
        gt = 1
        for i in range(1, self.a+1):
            gt *= i
        return gt


myList = []
myDict = {}
tongLP = 0
n = int(input("Nhap n"))
for i in range(n):
    a = int(input("Nhap a: "))
    obj = LuyThua(a)
    myList.append(obj)
    myDict[a] = obj.LapPhuong()
    tongLP += obj.LapPhuong()
    print(obj.GiaiThua())

print(tongLP)
print(myDict)
