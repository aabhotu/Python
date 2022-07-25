import math
n = int(input('Nhap n: '))


def giaTri():
    c1 = n
    c2 = 0
    min = 999
    for i in range(int(n/2)):
        c1 = c1-2
        c2 = c2+1
        if math.abs(c1-c2) < min:
            min = math.abs(c1-c2)
        else:
            break
        return min


print(giaTri())


giaTri()
