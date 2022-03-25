# nhập ngày tháng năm và tính khoảng cách từ ngày đó đến ngày 1/1/2000
import datetime
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
dis1 = datetime.datetime(2000, 1, 1)
print(dis1)
dis2 = datetime.datetime(year, month, day)
print(dis2)
if dis1 > dis2:
    tg = dis1-dis2
    print("So ngay: ", tg)
elif dis1 < dis2:
    tg = dis2 - dis1
    print("So ngay: ", tg)
else:
    print("la ngay 1/1/2000")
