n = int(input('Nhap n: '))
temp = n
soDaoNguoc = 0
while temp > 0:
    soDaoNguoc = soDaoNguoc * 10 + temp % 10
    temp = temp // 10
print(soDaoNguoc)
