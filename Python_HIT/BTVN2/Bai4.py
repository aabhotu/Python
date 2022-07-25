# n = int(input('Nhap n: '))
# # 1
# ph1 = 0
# for i in range(n):
#     ph1 += i
# print('Phan 1: ', ph1)

# #2
# ph2 = 0
# for i in range(n):
#     ph2 += 1/(2*i+1)
# print('Phan 2: ', ph2)

# #3
# ph3 = 0
# for i in range(n):
#     ph3 += i/(i+1)
# print('Phan 3: ', ph3)

# #4
# ph4 = 0
# x= float(input('Nhap x: '))
# for i in range(n):
#     ph4 += x**i
# print('Phan 4: ', ph4)

# #5
# a = float(input('Nhap a: '))
# b = float(input('Nhap b: '))

# if a == 0 and b == 0:
#     print('PTVSN')
# elif a == 0 and b != 0:
#     print('Phuong trinh vo nghiem: ')
# else:
#     print('Phuong trinh co nghiem: ', b/a)

# 6
ph6 = 0
i = 1
while ph6 < 10000:
    i += 1
    ph6 += i
print(i-1)

# 7
for i in range(65, 91):
    print(chr(i), end=' ')

for i in range(97, 123):
    print(chr(i), end=' ')

# 8
ph8 = int(input('\nNhap ph8:'))
check = 1
if ph8 < 2:
    check = 0
else:
    for i in range(2, ph8):
        if ph8 % i == 0:
            check = 0
            break
if check == 1:
    print('Ph8 la so nguyen to')
else:
    print('Ph8 khong phai la so nguyen to')
