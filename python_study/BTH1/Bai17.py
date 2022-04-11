def KiemtraNamNhuan(nam):
    return nam % 4 == 0 and nam % 100 != 0 or nam % 400 == 0


def TimNgayTrongThang(thang, nam):
    ngayTrongThang = 0
    if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
        ngayTrongThang = 31
    elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
        ngayTrongThang = 30
    elif thang == 2:
        if KiemtraNamNhuan(nam):
            ngayTrongThang = 29
        else:
            ngayTrongThang = 28
    return ngayTrongThang


def TimNgayTrc(ngay, thang, nam):
    ngayTrongThang = TimNgayTrongThang(thang, nam)
    if ngay == 1:
        ngay = ngayTrongThang
        if thang == 1:
            thang = 12
            nam -= 1
        else:
            thang -= 1
    else:
        ngay -= 1
        print('Ngay trc: %d/%d/%d' % (ngay, thang, nam))


day = int(input("Nhap ngay: "))
month = int(input("Nhap thang: "))
year = int(input("Nhap nam: "))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    while not 0 < day <= 31:
        day = int(input("Nhap ngay sai, nhap lai: "))
if month == 4 or month == 6 or month == 9 or month == 11:
    while not 0 < day <= 30:
        day = int(input("Nhap thang sai. nhap lai: "))
if (year % 400 == 0 or year % 4 == 0 and year % 100 != 0):
    if month == 2:
        while not 0 < day < 30:
            day = int(input("Nhap ngay sai. nhap lai: "))
else:
    if month == 2:
        while not 0 < day < 29:
            day = int(input("Nhap ngay sai. nhap lai: "))
print(TimNgayTrc(day, month, year))
