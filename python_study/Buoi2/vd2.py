def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)


def bcnn(a, b):
    return a*b//ucln(a, b)


x = int(input("Nhap x = "))
y = int(input("Nhap y = "))

print("BCNN(%d, %d) = %d" % (x, y, bcnn(x, y)))
