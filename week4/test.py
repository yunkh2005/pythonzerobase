for i in range(1, 10):
    print("i: ", i, end=' ')
    for j in range(2, 5):
        if j % 2 == 0:
            print("j: ", j)
        else:
            break