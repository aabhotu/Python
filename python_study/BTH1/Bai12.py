# erro
n = int(input('Nhap so n: '))
for i in range(1, n):
    a3 = i*i*i
    for j in range(1, n):
        b3 = j*j*j
        for k in range(1, n):
            c3 = k*k*k
            if a3 + b3 - c3 == 0:
                print(i, j, k)
