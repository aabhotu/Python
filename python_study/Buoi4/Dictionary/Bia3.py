# Nhập một dictionary có số phần tử ngẫu nhiên. Kết thúc nhập khi nhập key='y'
# Nhập một số x cùng kiểu với value. Tìm trong dic xem có bao nhiêu item
# có giá trị bằng x. xóa tất cả các item này

dict = {}
while True:
    key = input("Nhap key: ")
    if key == 't':
        break
    value = input("Nhap value: ")
    dict[key] = value
print(dict)
x = input("nhap x: ")
count = 0
for i in list(dict):
    if dict[i] == x:
        count += 1
        del dict[i]

print("The dictionary after remove is : " + str(dict))
print('so vi tri trung x: ' + str(count))
