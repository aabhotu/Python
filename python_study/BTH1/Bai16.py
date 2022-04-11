
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

s = day
for i in range(1, month):
    if i == 4 or i == 6 or i == 9 or i == 11:
        s += 30
    elif i == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            s += 29
        else:
            s += 28
    else:
        s += 31
print('Ngay thu %d trong nam' % s)
