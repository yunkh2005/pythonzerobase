def solution(n):
    num = set()                 # 중복이 불가능한 set을 생성
    
    while n not in num:         # num안에 n이 없을 때까지 반복
        num.add(n)              # num안에 n이 없으면 num에 저장
        n = sum([int(i) ** 2 for i in str(n)])
        print(n)

        if n == 1:
            return True
    
    return False

# Test code
print(solution(19)) # True
print(solution(61)) # False