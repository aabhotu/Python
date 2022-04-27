myList = []

n = int(input('Nhap so phan tu mang: '))

for i in range(n):
    myList.append(float(input('Nhap phan tu thu '+str(i)+': ')))

x = float(input("Nhap x: "))

length = len(myList)
index = 0
while index <= length:
    if myList[index] == x:
        myList.insert(index, x)
        index += 2
    else:
        index += 1

print("Mang sau khi chen: ", myList)
