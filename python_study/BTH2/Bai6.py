str = []
n = int(input('Nhap so phan tu: '))
for i in range(n):
    str.append(input('Nhap phan tu thu %d: ' % (i+1)))
print('Cac phan tu vua nhap la: ', str)

myTuple = ()
for i in range(n):
    if str[i] >= 'A' and str[i] <= 'Z':
        myTuple += (str[i],)
print('Cac chu hoa vua nhap la: ', myTuple)
