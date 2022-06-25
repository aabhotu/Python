class NhanVien():
    def __init__(self, hoTen, namCT, luongCB, hsLuong):
        self.hoTen = hoTen
        self.namCT = namCT
        self.luongCB = luongCB
        self.hsLuong = hsLuong

    def TinhLuong(self):
        return self.luongCB*self.hsLuong+self.namCT*self.luongCB*0.1

    def output(self):
        print("\nTHONG TIN")
        print("Ho ten: " + self.hoTen)
        print("So nam cong tac: " + str(self.namCT))
        print("Luong co ban: " + str(self.luongCB))
        print("He so luong: "+str(self.hsLuong))


myList = []
TimMax = []

for i in range(3):
    print("Nhap nv: ")
    hoten = input("Nhap ten: ")
    namCt = int(input("Nhap sp nam ct: "))
    luongCB = int(input("Nhap luong: "))
    hsLuong = int(input("NHap he so luong: "))
    TimMax.append(namCt)
    obj = NhanVien(hoten, namCt, luongCB, hsLuong)
    myList.append(obj)

for i in range(3):
    myList[i].output()

print("max la: " + str(max(TimMax)))
