import math


def CanB2(a):
    return math.sqrt(a)


def BinhPhuong(a):
    return a*a


class DiemTD:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def input(self):
        self.x = int(input("nhap hoanh do x: "))
        self.y = int(input("nhap tung do y: "))


def KhoangCach(a, b):
    kc = math.sqrt((b.x-a.x)**2+(b.y-a.y)**2)
    return kc


def TamGiac(a, b, c):
    if a+b > c or a+c > b or b+c > a:
        return True
    else:
        return False


def ChuVi(a, b, c):
    if TamGiac(a, b, c):
        return a+b+c
    else:
        return "Khong phai la tam giac"


def DienTich(a, b, c):
    if TamGiac(a, b, c):
        nuaCV = ChuVi(a, b, c)/2
        return math.sqrt(nuaCV*(nuaCV-a)*(nuaCV-b)*(nuaCV-c))
    else:
        return "Khong phai la tam giac"


def TamGiacTD():
    a = DiemTD(0, 0)
    print('Nhap toa do diem a: ')
    a.input()
    b = DiemTD(0, 0)
    print('Nhap toa do diem b: ')
    b.input()
    c = DiemTD(0, 0)
    print('Nhap toa do diem c: ')
    c.input()

    if TamGiac(KhoangCach(a, b), KhoangCach(b, c), KhoangCach(c, a)):

        print('Chu vi: ', ChuVi(KhoangCach(a, b),
              KhoangCach(b, c), KhoangCach(c, a)))
        print('Dien tich: ', DienTich(KhoangCach(a, b),
              KhoangCach(b, c), KhoangCach(c, a)))
    else:
        print("Khong phai la tam giac")


TamGiacTD()
