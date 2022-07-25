import datetime

ngay = int(input('Nhap ngay: '))
thang = int(input('Nhap thang: '))
nam = int(input('Nhap nam: '))


d1 = datetime.datetime(nam, thang, ngay)
d2 = datetime.datetime(nam, 12, 31)
d3 = d2 - d1
print(d3)
