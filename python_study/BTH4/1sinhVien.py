


class sinhVien():
    def __init__(self, ten, namSinh, diemToan, diemVan, diemNN):
        self.ten=ten
        self.namSinh=namSinh
        self.diemToan=diemToan
        self.diemVan=diemVan
        self.diemNN=diemNN
        return
    def tongDiem(self):
        tong=self.diemToan+self.diemVan+self.diemNN
        return tong
    def xuat(self):
        print("ten: ", self.ten, "\nnam sinh: ", self.namSinh, "\ndiem toan: ", self.diemToan, "\ndiem van: ", self.diemVan, "\ndiem ngoai ngu: ", self.diemNN)
def sapXep(a):
    for i in range(len(a)):
        m=i
        for j in range((i+1), len(a)):
            if(a[j].tongDiem()>a[m].tongDiem()):
                m=j
        if(m!=i):
            t=a[i]
            a[i]=a[m]
            a[m]=t

a=[]
n=int(input("nhap so sinh vien: "))
while n<1:
    n=int(input("nhap so nhan vien: "))
for i in range(n):
    print("sinh vien thu %d" %(i+1))
    ten=input("ten: ")
    ns=int(input("nam sinh: "))
    t=float(input("diem toan: "))
    v=float(input("diem van: "))
    nn=float(input("diem ngoai ngu: "))
    a.append(sinhVien(ten, ns, t, v, nn))
#b=sorted(a, KEY=sinhVien.diemToan, reverse=False)
sapXep(a)
print("sinh vien sap xep theo tong diem giam dan: ")
for i in range(len(a)):
    print(a[i].ten)
tongToan=0
tongVan=0
tongNN=0
for i in range(len(a)):
    tongToan=tongToan+a[i].diemToan
    tongVan=tongVan+a[i].diemVan
    tongNN=tongNN+a[i].diemNN
print("tbc diem toan: ", tongToan/n, "\ntbc diem van: ", tongVan/n, "\ntbc diem ngoai ngu: ", tongNN/n)



