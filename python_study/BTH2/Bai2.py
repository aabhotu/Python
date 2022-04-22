x = []

count = 0
n = int(input('Nhap so phan tu: '))
for i in range(n):
    x.append(int(input('Nhap phan tu thu ' + str(i+1) + ': ')))


def SoDoiXung(n):
    temp = n
    sdx = 0
    while temp > 0:
        sdx = sdx*10 + temp % 10
        temp //= 10
    if sdx == n:
        return True
    else:
        return False


for i in range(n):
    if SoDoiXung(x[i]):
        count += 1
for i in range(n):
    for j in range(i+1, n):
        if SoDoiXung(x[i]) and SoDoiXung(x[j]) and x[i] > x[j]:
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
        elif SoDoiXung(x[i]) == False and SoDoiXung(x[j]) == False and x[i] < x[j]:
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
print('So phan tu doi xung: ', count)
print('Mang sau khi sap xep: ', x)
