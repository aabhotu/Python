class SoNguyen():
    def __init__(self, a):
        self.a = a

    def Dem(self):
        b = list(self.a)
        b.reverse()
        # print(b)
        dem = 0
        for i in range(len(b)):
            if b[i] == '.':
                break
            else:
                dem += 1
        print(dem)


n = input()
m = SoNguyen(n)
m.Dem()
