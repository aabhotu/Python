from re import A


a = int(input('Nhap n: '))
b = int(input('Nhap m: '))
n = a
m = b
while m > 0 and n > 0:
    if n > m:
        n = n - m
    else:
        m = m - n
print('Uoc chung lon nhat la: ', max(n, m))
print('Boi chung nho nhat la: ', (a*b)/max(n, m))
