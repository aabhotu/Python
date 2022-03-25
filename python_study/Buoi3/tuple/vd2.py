# chính phương  trong khoảng từ 1-n
import math
n = int(input('nhap so phan tu: '))
myTuple = ()
for i in range(1, n):
    if math.sqrt(i) * math.sqrt(i) == i:
        myTuple = myTuple + (i,)
print(myTuple)
