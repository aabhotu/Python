
a1 = int(input('nhap a1: '))
b1 = int(input('nhap b1: '))
c1 = int(input('nhap c1: '))
a2 = int(input('nhap a2: '))
b2 = int(input('nhap b2: '))
c2 = int(input('nhap c2: '))
d = a1*b2-a2*b1
dx = c1*b2-c2*b1
dy = a1*c2-a2*c1
if d == 0:
    if(dx == 0 or dy == 0):
        print('pt vo so nghiem')
    else:
        print('pt vo nghiem')
else:
    x = dx/d
    y = dy/d
    print('pt co nghiem x=', x, 'y=', y)
