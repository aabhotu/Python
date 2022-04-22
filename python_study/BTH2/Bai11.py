n = int(input('Nhap so nguyen dương: '))
myTuple = (0, 1)

while n < 0:
    print("Nhap lai n: ")
    n = int(input('Nhap so nguyen dương: '))
for i in range(n):
    for j in range(i):
        if j**3 == i:
            myTuple += (i,)
print('My tuple: ', myTuple)
