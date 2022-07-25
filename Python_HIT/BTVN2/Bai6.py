n = int(input('nhap so phan tu:'))
a = []
for i in range(n):
    a.append(int(input('nhap phan tu:')))
print(a)

tongChan = 0
tongLe = 0

for i in range(n):
    if a[i] % 2 == 0:
        tongChan += a[i]
    else:
        tongLe += a[i]
if tongChan > tongLe:
    print('even')
else:
    print('odd')
