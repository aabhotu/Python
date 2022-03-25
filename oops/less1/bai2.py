class HCN:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def nhap(self):
        self.dai = int(input("Nhap dai: "))
        self.rong = int(input("Nhap rong: "))

    def ve(self):
        for h in range(self.rong):
            for w in range(self.dai):
                if h == 0 or w == 0 or h == self.rong - 1 or w == self.dai - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print("")

    def chuvi(self):
        return (self.dai + self.rong)*2

    def dientich(self):
        return self.dai * self.rong


rect = HCN(0, 0)
rect.nhap()
rect.ve()
print("Chu vi: ", rect.chuvi())
print("Dien tich: ", rect.dientich())
