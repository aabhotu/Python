class nhanVien():
    def __init__(self, ten, namSinh, namVao):
        self.ten=ten
        self.namSinh=namSinh
        self.namVao=namVao
        return
    def tuoi(self):
        t=2022-self.namSinh
        return t
    def namCtac(self):
        ct=2022-self.namVao
        return ct
    def xuatNhanVien(self):
        print("ten: ", self.ten, " \ntuoi ", self.tuoi(), "\nnam con tac: ", self.namCtac())

class chuyenVien(nhanVien):
    def __init__(self, luongCB, tDo):
        super().__init__(self, luongCB, tDo)
        self.luongCB=luongCB
        self.tDo=tDo
        return
    def heSo(self):
        if self.tDo=="Tien Si":
            return 5
        elif self.tDo=="Thac Si":
            return 4
        elif self.tDo=="Dai Hoc":
            return 3
        elif self.tDo=="Cao Dang":
            return 2
        else:
            return 1
    def luong(self):
        return (self.heSo()*self.namCtac()*self.luongCB)
    
a=[]
n=int(input("so nhan vien: "))
while(n<1):
    n=int(input("so nhan vien? "))
for i in range(0,n):
    print("nhap thong tin nhan vien thu %d: " %(i+1))
    t=input("ten: ")
    ns=int(input("nam sinh: "))
    nv=int(input("nam vao lam viec: "))
    a.append(nhanVien)
    