n = int(input('Nhap n: '))
s = 0
p = 1
x = float(input('x: '))
for i in range(1, n+1):
    p = p*i
    s += ((-1)**i)*(x**i) / p
print(s)
