# a = int(input())
# max = a
# while a != 0:
#     if a > max:
#         max = a
#     a = int(input())
# print(max)

# dem so chan duong
a = int(input())
dem = 0
while a != 0:
    if a % 2 == 0 and a > 0:
        dem += 1
    a = int(input())
print(dem)
