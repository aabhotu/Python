import re
a = str(input('Nhap chuoi: '))

so = re.findall('\d+', a)
print(so)
tong = 0
for i in range(len(so)):
    tong += int(so[i])
print(tong)
