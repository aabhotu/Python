# nhập 1 list và 1 số x. đếm có bn số bằng x, hiển thị vị trí, xóa số bằng x
# nhg để lại số đầu
myList = []
newList = []
dem = 0
x = float(input('nhap so x: '))
n = int(input('nhap so phan tu: '))
for i in range(n):
    a = float(input('nhap phan tu thu '+str(i+1)+': '))
    myList.append(a)
print('vi tri bang x: ')
for i in range(len(myList)):
    if myList[i] == x:
        dem += 1
        print(i, end=' ')
        newList.append(i)
print('\nso luong so bang x: ', dem)
print(newList)
try:
    for i in range(1, len(newList)):
        myList.pop(newList[i])
except:
    myList.pop(len(myList)-1)
print('\nlist sau khi xoa: ', myList)
