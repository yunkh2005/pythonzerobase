a = [0]
for i in range(11):
    a.append(i)

print(a[0], end=' ')
for i in range(1, len(a)):
    if (2 ** a[i]) <= 256:
        print(2 ** a[i], end=' ')
    else:
        print(256, end=' ')