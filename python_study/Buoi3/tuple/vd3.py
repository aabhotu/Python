# tách 1 mảng thành hai mảng chứa số âm và số dương riêng biệt
myList = []
soAm = ()
soDuong = ()
n = int(input('nhap so phan tu: '))
for i in range(n):
    a = float(input('nhap phan tu thu '+str(i+1)+': '))
    myList.append(a)
for i in range(len(myList)):
    if myList[i] > 0:
        soDuong = soDuong + (myList[i],)
    else:
        soAm = soAm + (myList[i],)
print('so duong: ', soDuong)
print('so am: ', soAm)
