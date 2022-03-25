# nhập 1 list các số thực, tìm max, đếm max và trị trí max
myList = []
n = int(input('nhap so phan tu: '))
for i in range(n):
    a = int(input('nhap phan tu thu '+str(i+1)+': '))
    myList.append(a)
soMax = max(myList)
print('so lon nhat: ', soMax)
soLuongMax = myList.count(soMax)
print('so luong so lon nhat: ', soLuongMax)
print('vi tri so phan tu max: ')
for i in range(len(myList)):
    if myList[i] == soMax:
        print(i+1, end=' ')
