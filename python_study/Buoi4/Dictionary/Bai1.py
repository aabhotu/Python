# tạo một dictionary gồm có các số nguyên từ 1 đến n (n nhập từ bàn phím),
# value là bình phương của các số đó

A = {}
n = int(input("Nhap n: "))
for i in range(1, n+1):
    A[i] = i**2
print(A)
