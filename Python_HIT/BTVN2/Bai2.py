import math

n = int(input("Nhập số n: "))
f = 0
if n % 2 == 0:
    for i in range(n):
        f += 1/(2 ** i)
else:
    f = math.sqrt(n ** 2+1)
print(f)
