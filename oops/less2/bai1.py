class Date:
    def __init__(self):
        self.day = ''
        self.month = ''
        self.year = ''

    def input(self):
        self.day = int(input("Nhap ngay: "))
        self.month = int(input("Nhap thang: "))
        self.year = int(input("Nhap nam: "))

    def output(self):
        print(f"Date: {self.day}/{self.month}/{self.year}")


class NhanSu:
    def __init__(self):
        self.MaNhanSu = ''
        self.HoTen = ''
        self.date = Date()

    def input(self):
        self.date.input()
        self.MaNhanSu = input("Nhap ma nhan su: ")
        self.HoTen = input("Nhap ho ten: ")

    def output(self):
        self.date.output()
        print(f"Ma nhan su: {self.MaNhanSu}")
        print(f"Ho ten: {self.HoTen}")


employee = NhanSu()
employee.input()
employee.output()
