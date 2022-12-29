def countUniques(a):
    num = 1                 # 서로 다른 값 개수
    if len(a) == 1:         # 매개변수 길이가 1일 때
        return num  

    temp = a[0]
    for i in range(1, len(a)):
        if temp != a[i]:
            temp = a[i]
            num += 1
    
    return num

# Test code
print(countUniques([-1, 1, 1, 1, 1, 4, 4, 4, 4, 10, 14, 14])) # 5
print(countUniques([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) # 2