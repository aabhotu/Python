myList = []
n = int(input('Nhap so phan tu: '))
for i in range(n):
    myList.append(int(input('Nhap phan tu thu %d: ' % (i+1))))
increase = myList.copy()
decrease = myList.copy()

for i in range(n):
    for j in range(i+1, n):
        if increase[i] > increase[j]:
            temp = increase[i]
            increase[i] = increase[j]
            increase[j] = temp

for i in range(n):
    for j in range(i+1, n):
        if decrease[i] < decrease[j]:
            temp = decrease[i]
            decrease[i] = decrease[j]
            decrease[j] = temp
# decrease = myList.reserve()

print('Increase: ', increase)
print('Decrease: ', decrease)

increase.remove(increase[0])
increase.remove(increase[-1])
print('Sau khi xoa increase: ', increase)

decrease.remove(decrease[0])
decrease.remove(decrease[-1])
print('Sau khi xoa decrease: ', decrease)
