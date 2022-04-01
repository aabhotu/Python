from file1 import *
list1 = []
cp = 0
tongCP = 0
snt = 0
tongNT = 0
sd = 0
tongSD = 0
n = int(input("Nhập số phần tử của list: "))
for i in range(n):
    list1.append(int(input("Nhập phần tử thứ %d: " % (i+1))))

for i in range(n):
    if SoChinhPhuong(list1[i]):
        # print(list1[i])
        cp += 1
        tongCP += list1[i]

for i in range(n):
    if soNguyenTo(list1[i]):
        # print(list1[i])
        snt += 1
        tongNT += list1[i]

for i in range(n):
    if SoDao(list1[i]):
        # print(list1[i])
        sd += 1
        tongSD += list1[i]

print(cp)
if cp == 0:
    print("Không có số nào có thể là số chính phương")
else:
    print("Trung bình cộng cp là: ", tongCP/cp)

print("so nt: ", snt)
if snt == 0:
    print("Không có số nào có thể là số nguyên tố")
else:
    print("Trung bình cộng snt là: ", tongNT/snt)

print("so dao: ", sd)
if sd == 0:
    print("Không có số nào có thể là số đảo")
else:
    print("Trung bình cộng sd là: ", tongSD/sd)
