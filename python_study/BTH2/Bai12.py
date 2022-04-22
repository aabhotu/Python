myList = []
n = int(input('Nhap so phan tu: '))
for i in range(n):
    myList.append(int(input('Nhap phan tu thu ' + str(i+1) + ': ')))


def checkSCP(n):
    for i in range(n):
        if i*i == n:
            return True
    return False


index = 0
while index <= n:
    if (checkSCP(myList[index])):
        myList.insert(index, 0)
        index += 2
    else:
        index += 1
if(myList[len(myList)-1] == myList[len(myList)-2]):
    myList.insert(len(myList)-1, 0)

print('Mang sau khi chen: ', myList)
