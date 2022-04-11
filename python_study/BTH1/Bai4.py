n = int(input('Nhap n: '))
s = 0
for i in range(1, n+1):
    if n % i == 0:
        s += i
if n*2 == s:
    print('La so hoan thien: ')
else:
    print('Khong phai la so hoan thien')
