myList = []


def ucln(a, b):
    if(a == b):
        return a
    else:
        if (b > a):
            return ucln(b-a, a)
        else:
            return ucln(a-b, b)


def bcnn(a, b):
    return (a*b)//ucln(a, b)


def uclnMang(a, n):
    if(n == 1):
        return a[0]
    else:
        return ucln(a[n-1], uclnMang(a, n-1))


def bcnnMang(a, n):
    temp = bcnn(a[0], a[1])
    for i in range(2, n):
        temp = bcnn(temp, a[i])
    return temp


n = int(input('Nhap so phan tu: '))
for i in range(n):
    myList.append(int(input('Nhap phan tu thu %d: ' % (i+1))))
print('UCLN: ', uclnMang(myList, n))
print('BCNN: ', bcnnMang(myList, n))
