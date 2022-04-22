
x = []
y = []
n = int(input('Nhap so phan tu: '))
for i in range(n):
    x.append(float(input('Nhap phan tu thu ' + str(i)+':')))
max = x[0]
for i in range(n):
    if x[i] > max:
        max = x[i]

print('Max: ', max)

try:
    for i in range(n):
        while x[i] == max:
            x.remove(max)

            # x[i] = x[i+1]
            # n -= 1

except:
    # x.pop(len(x)-1)
    print(' ')
print('List sau khi xoa: ', x)
