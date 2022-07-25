import math
x = float(input('Nhap x: '))
f = (x**2 + math.e**x + math.sin(x)) / math.sqrt(x**2+1)
print('Gia tri bieu thuc: ' + str(round(f)))
