import math
a = int(input('nhap a: '))
b = int(input('nhap b: '))
c = int(input('nhap c: '))
if a == 0:
    if b == 0:
        print('pt vo nghiem')
    else:
        print('pt co 1 nghiem x=', -c/b)
else:
    delta = (b*b-4*a*c)/2
    if delta < 0:
        print('vo nghiem')
    elif delta == 0:
        x = -b/2/a
        print('nghiem kep: ' + str(x))
    else:
        x1 = (-b+math.sqrt(delta))/2/a
        x2 = (-b-math.sqrt(delta))/2/a
        print('nghiem phan biet: ' + str(x1) + ' va ' + str(x2))
