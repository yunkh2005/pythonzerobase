a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = lambda x: x * x
c = list()
for elem in a:
    c.append(b(elem))
print(c)