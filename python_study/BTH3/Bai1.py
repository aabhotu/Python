List1 = []
List2 = []
n = int(input("Nhap n: "))
for i in range(1, n+1):
    List1.append(i)
for i in range(1, n+1):
    x = int(input("Nhap phan tu: "))
    List2.append(x)
dict = {}
for i in range(len(List1)):
    dict[List1[i]] = List2[i]
print(dict)
