
x = []
snt = []
scp = []
conLai = []


def checkSNT(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def checkSCP(n):
    for i in range(n):
        if i**2 == n:
            return True
    return False


n = int(input('Nhap so phan tu: '))
for i in range(n):
    x.append(int(input('Nhap phan tu thu '+str(i+1)+': ')))
print('x ', x)
for i in range(n):
    if checkSNT(x[i]):
        snt.append(x[i])
    elif checkSCP(x[i]):
        scp.append(x[i])
    else:
        conLai.append(x[i])
print('SNT: ', tuple(snt))
print('SCP: ', tuple(scp))
print('Con lai: ', tuple(conLai))
