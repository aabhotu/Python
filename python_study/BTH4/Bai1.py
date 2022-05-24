class SinhVien:
    def __init__(self, hoTen, namSinh, diemToan, diemVan, diemNN):
        hoTen = ''
        namSinh = ''
        diemToan = 0
        diemVan = 0
        diemNN = 0

    def input(self):
        self.hoTen = input('Nhap ho ten: ')
        self.namSinh = input('Nhap nam sinh: ')
        self.diemToan = int(input('Nhap diem toan: '))
        self.diemVan = int(input('Nhap diem van: '))
        self.diemNN = int(input('Nhap diem ngoai ngu: '))

    def output(self):
        print('{:<20} {:<10} {:<10} {:<10} {:<10} '.format(
            self.hoTen, self.namSinh, self.diemToan, self.diemVan, self.diemNN))


def tbc(self, myList):
    tong = 0
    for i in myList:
        tong = tong + myList[i]
    return tong/len(myList)
