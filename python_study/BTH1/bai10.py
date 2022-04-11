n = str(input('Nhap n: '))
string = []
cnt = []
for i in range(len(n)):
    string.append(n[i])
for i in range(len(string)):
    if string[i] not in cnt:
        cnt.append(string[i])
for i in range(len(string)):
    for j in range(len(cnt)):
        if string[i] == cnt[j]:
            cnt[j] = cnt[j] + ':' + str(string.count(string[i]))
for i in range(len(cnt)):
    print(cnt[i])
