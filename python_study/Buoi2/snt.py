n = int(input())
if n < 2:
    print('ko ph snt')
else:
    for i in range(2, n):
        if (n % i == 0):
            print('ko ph snt')
            break
        else:
            print('la snt')
