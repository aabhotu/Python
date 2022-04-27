
mylist = []
demDuong = 0
demAm = 0
tongduong = 0
tongam = 0
n = int(input("Nhap so phan tu cua list: "))
for i in range(0, n):
    x = float(input("Nhap phan tu thu %d: " % (i+1)))
    mylist.append(x)
for i in range(len(mylist)):
    if mylist[i] > 0:
        demDuong += 1
        tongduong += mylist[i]
    else:
        demAm += 1
        tongam += mylist[i]
if demDuong > 0:
    print('so phan tu duong: ' + str(demDuong))
    print("Trung binh cong cac phan tu duong: ", tongduong/demDuong)
else:
    print("Khong co phan tu duong")
if demAm > 0:
    print('so phan tu am: ' + str(demAm))
    print("Trung binh cong cac phan tu am: ", tongam/demAm)
else:
    print("Khong co phan tu am")
