# nhập vào một list và đếm phần tử âm, phần tử dương + tính tbc cá phần
# tử âm, tbc các phần tử dương
mylist = []
demChan = 0
demLe = 0
listChan = []
listLe = []
try:
    n = int(input("Nhap so phan tu cua list: "))
except ValueError:
    print("Nhap sai! Nhap lai!")
for i in range(0, n):
    x = float(input("Nhap phan tu thu %d: " % (i+1)))
    mylist.append(x)
for i in range(len(mylist)):
    if mylist[i] % 2 == 0:
        demChan += 1
        listChan.append(mylist[i])
    else:
        demLe += 1
        listLe.append(mylist[i])
if demChan > 0:
    print('so phan tu chan: ' + str(demChan))
    print(listChan)
else:
    print("Khong co phan tu chan")
if demLe > 0:
    print('so phan tu le: ' + str(demLe))
    print(listLe)
else:
    print("Khong co phan tu le")
