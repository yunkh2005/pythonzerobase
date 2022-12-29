'''
문자열을 뒤에서부터 읽어도 원래 문자열과 같은 단어를 팰린드롬이라 한다.
입력으로 주어진 문자열이 팰린드롬인지 판별한 뒤, 
팰린드롬이면 빈 문자열을 출력한다.
입력된 문자열이 팰린드롬이 아닐 경우 
문자열을 반으로 나누어 앞부분의 단어를 기준으로 
팰린드롬 단어로 만드는 함수를 작성하시오.

예시 입력1
입력: s = 'abcdcba'
출력: ''

예시 입력2
입력: s = 'bannana'
출력: 'bannab'

예시 입력3
입력: s = 'wabe'
출력: 'waaw'

'''
def solution(s):
    str_list = list(s)
    if str_list == str_list[::-1]:
        return ''
    else:
        q, r = divmod(len(str_list), 2) # 몫, 나머지
        front = str_list[:q]
        if r%2 == 0:
             result = front + front[::-1]
        else:
            result = front + [str_list[q]] + front[::-1]
        return(''.join(result))

s = 'abccba'
print(solution(s))  # ''

s = 'bannana'
print(solution(s))  # 'bannab'

s = 'wabe'
print(solution(s))  # 'waaw'