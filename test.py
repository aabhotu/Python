a = 'AEGFDGFECEDHGCHEGEEGEDHGEEGEHADEEDDGEDEGADCDGAADFAFDCACBFBCFCCBC'
print(len(a))
count = 0
for i in range(len(a)):
    if a[i] == 'A':
        count += 1
print(count)
