# nhập vào 2 list, list 1chỉ chứa các số nguyên, list 2 chứa danh sách tên các môn học
# trong học kì hiện tại. Tạo 1 dic bằng cách: ky là các phần tử của list 1, value
# là các phần tử của list 2.

# List1 = [1, 2, 3, 4, 5]
# List2 = ['toán', 'lý', 'hoá', 'sinh', 'văn']
List1 = []
List2 = []
n = int(input("Nhap n: "))
for i in range(1, n+1):
    List1.append(i)
for i in range(1, n+1):
    x = str(input("Nhap ten mon hoc: "))
    List2.append(x)
dict = {}
for i in range(len(List1)):
    dict[List1[i]] = List2[i]
print(dict)
