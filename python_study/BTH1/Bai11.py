n = str(input('Nhap chuoi: '))
chuoi = n.split(',')
n = ' '.join(chuoi)

chuoi = n.split('.')
n = ' '.join(chuoi)

chuoi = n.split(' ')
chuoi2 = []
for i in range(len(chuoi)):
    if chuoi[i] == '':
        continue
    else:
        chuoi2.append(chuoi[i])
print(chuoi2)
print('Chieu dai chuoi: ', len(chuoi2))
for i in range(len(chuoi2)):
    chuoi2[i] = str(chuoi2[i]).capitalize()
n = ' '.join(chuoi2)
print('Chuoi sau khi chuan hoa: ', n)
