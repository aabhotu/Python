n = int(input('Nhap n: '))
check = 1
if n == 1:
    check = 0
else:
    for i in range(2, n):
        if n % i == 0:
            check = 0
            break
if check == 0:
    print('Ko ph so nguyen to')
else:
    print('So nguyen to')
