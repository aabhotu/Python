myList = []
n = int(input('Nhap so phan tu: '))
for i in range(n):
    myList.append(int(input('Nhap phan tu thu %d: ' % (i+1))))


def CheckTG(a, b, c):
    if a+b > c or a+c > b or b+c > a:
        return True
    else:
        return False


for i in range(len(myList)):
    for j in range(i+1, len(myList)):
        for k in range(j+1, len(myList)):
            if CheckTG(myList[i], myList[j], myList[k]):
                print(myList[i], myList[j], myList[k])
