myList = []
myTuple = ()
n = int(input('Nhap so phan tu: '))
for i in range(n):
    myList.append(input('Nhap phan tu thu %d: ' % (i+1)))


def CheckSNT(n):
    check = 1
    if n == 1:
        check = 0
    else:
        for i in range(2, n):
            if n % i == 0:
                check = 0
        return check


for i in range(len(myList)):
    if CheckSNT(int(myList[i])) == 1:
        myTuple += (myList[i],)

print('My tuple: ', myTuple)
