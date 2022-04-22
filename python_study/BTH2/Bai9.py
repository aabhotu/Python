x = int(input('Nhap x: '))
y = int(input('Nhap y: '))
myTuple = ()

for i in range(x, y):
    if i % 2 == 0 and i % 3 == 0:
        myTuple += (i,)
print('My tuple: ', myTuple)
