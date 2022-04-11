from re import I


n = int(input('Nhap n: '))
s = 0
p = 1
i = 1
while i <= n:
    p = p*i
    s += p
    i += 1
print(s)
