# dem = tong = 0
# a = int(input())
# while a != 0:
#     dem += 1
#     tong += a
#     a = int(input())
# print(tong/dem)
password = input("nhap pass: ")
name = input('nhap name: ')
i = 1
while (password != '1234') and (name != 'abc'):
    password = input("nhap lai pass: ")
    name = input('nhap lai name: ')
    i += 1
    if i == 3:
        print('ban da nhap sai 3 lan')
        break

if password == '1234' and name == 'abc':
    print('Hello', name)
