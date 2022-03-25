class SinhVien:
    def __init__(self, MaSV, HoTen, Tuoi, Diem):
        self.MaSV = MaSV
        self.HoTen = ''
        self.Tuoi = 0
        self.Diem = 0

    def nhap(self):
        self.MaSV = input("Nhap MaSV: ")
        self.HoTen = input("Nhap HoTen: ")
        self.Tuoi = input("Nhap Tuoi: ")
        self.Diem = float(input("Nhap Diem: "))

    def Xuat(self):
        print("{:<10} {:<10} {:<15} {:<5}".format(
            "Ma SV", "Ho Ten", "Tuoi", "Diem"))
        print("{:<10} {:<12} {:<5} {:<5}".format(
            self.MaSV, self.HoTen, self.Tuoi, self.Diem))


student = SinhVien(1, 2, 3, 4)
student.nhap()
student.Xuat()
