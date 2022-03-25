# số chia hết cho 5 và 7 trong khoảng từ 1-n
n = int(input('nhap so phan tu: '))
myTuple = ()
for i in range(n):
    if i % 5 == 0 and i % 7 == 0:
        myTuple = myTuple + (i,)
print(myTuple)
