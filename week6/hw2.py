def solution(N, number):
    answer = -1
    arr = []

    for i in range(1, 9):
        num = set()
        num.add(int(str(N) * i))
        
        for j in range(0, i - 1):
            for x in arr[j]:
                for y in arr[(-j) - 1]:
                    num.add(x + y)
                    num.add(x - y)
                    num.add(x * y)
                    
                    if y != 0:
                        num.add(x // y)

        if number in num:
            answer = i
            break
        
        arr.append(num)

    return answer

print(solution(5, 12))      # 4
print(solution(2, 11))      # 3