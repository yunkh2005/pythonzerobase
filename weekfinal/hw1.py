def solution(s):
    mid = len(s) // 2

    def change(s):
        str = s[:mid]
        s = str + str[::-1]
        return s

    # 홀수
    if len(s) % 2 != 0:         
        if s[:mid] == s[:mid:-1]:
            return ''
        else:
            return change(s)
    # 짝수
    else:
        if s[:mid] == s[:(mid-1):-1]:
            return ''
        else:   
            return change(s)

s = 'abccba'
print(solution(s))  # ''

s = 'bannana'
print(solution(s))  # 'bannab'

s = 'wabe'
print(solution(s))  # 'waaw'