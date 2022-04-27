myDict = {}
n = int(input('Nhap so phan tu: '))


def TimSV(myDict):
    value = str(input('Nhap ten SV can tim: '))
    for i in myDict:
        if(myDict[i] == value):
            print('SV %s co ma %d' % (value, i))
            break


def TimKey(myDict):
    key = int(input('Nhap key can tim: '))
    for i in myDict:
        if(i == key):
            print('SV %s co ma %d' % (myDict[i], key))
            break


for i in range(n):
    myDict[i] = str(input('Nhap ten sinh vien %d: ' % (i+1)))

a = TimSV(myDict)
b = TimKey(myDict)
