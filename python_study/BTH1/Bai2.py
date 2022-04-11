n = int(input('Nhap n: '))
temp = n
count = 0
while temp != 0:
    count += 1
    temp //= 10
print('So chu so: ', count)
