'''
과제 3

민수는 최근 숫자 세기 놀이에 푹 빠져있다. 
민수는 숫자를 N진수로 세며, 
9보다 큰 숫자는 한자리로 표현하기 위해 아래와 같이 바꾸어서 센다.
10 ~ 35: a~z (알파벳 소문자)
36 ~ 61: A~Z (알파벳 대문자)
민수가 N진수의 숫자를 start부터 end까지 센 결과를 counts라고 할 때, 
민수가 잘 못 센 숫자의 개수를 반환하는 함수를 구현하시오.
(단, 2 < N <= 62, start < end이며, 
counts의 길이는 (end - start + 1)이다.)

입출력 예시
N	start	end	    counts	                    return
14	'9'	    'd'	    ['9', 'a', 'c', 'd', 'e']	3
62	'Z'	    '12'	['Z', '10', '11', '12']	    0
'''

def solution(N, start, end, counts):
    mapper = {
      str(x):x for x in range(10)
    }
    offset = len(mapper)
    mapper.update({
        chr(x):x - ord('a') + offset for x in range(ord('a'), ord('z') + 1)
    })
    offset = len(mapper)
    mapper.update({
        chr(x):x - ord('A') + offset for x in range(ord('A'), ord('Z') + 1)
    })
    
    def todec(s):
        val = 0
        for i, n in enumerate(s[::-1]):
            val += mapper[n] * N**i
        return val
    answer = 0

    start = todec(start)
    end = todec(end)
    
    for s, target in zip(counts, range(start, end + 1)):

        if todec(s) != target:
            answer += 1

    return answer

print(solution(14, '9', 'd', ['9', 'a', 'c', 'd', 'e']))    # 3
print(solution(62, 'Z', '12', ['Z', '10', '11', '12']))     # 0
