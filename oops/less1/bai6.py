class array:
    arr = []

    def __init__(self, n):
        self.n = 0
        self.arr = []

    def input(self):
        self.n = int(input("Nhap so phan tu: "))
        if self.n > 0:
            for i in range(self.n):
                self.arr.append(int(input("Nhap phan tu thu {}:".format(i))))
        else:
            print("Nhap lai: ")

    def output(self):
        print(self.arr)

    def timMax(self):
        print(max(self.arr))

    def timMin(self):
        print(min(self.arr))


arr1 = array(5)
arr1.input()
arr1.output()
arr1.timMax()
arr1.timMin()
