'''
과제 4

정수로 이루어진 수열 x가 주어졌을 때, 
x[i-1] < x[i], x[i+1] < x[i]인 x[i]를 피크라고 부른다. 
수열 x에 피크가 단 하나 반드시 존재할 때, 
이 피크를 찾아 출력하는 O(logN) 알고리즘을 구현하시오. 
(단, 수열 x의 길이가 N일 때, 반드시 x[0] <= x[1]이며, 
  x[N-1] <= x[N-2]이다.)

예시 입력
x	                                            return
[-4, -4, -2, 0, 0, 2, 4, 5, 6, 3, 2, -4, -6]	6
[-1, -1, -1, -1, 0, 1, 20, 19, 17]	            20
'''

def solution(x):
    n = len(x)

    if n < 3:
        return None

    mid = x[n//2 - 1 : n // 2 + 2]
    left = x[:n//2 + 1]
    right = x[n//2:]

    if mid[0] < mid[1] and mid[1] > mid[2]:
        return mid[1]
    elif mid[0] > mid[1]:
        return solution(left)
    else:
        return solution(right)

print(solution([-4, -4, -2, 0, 0, 2, 4, 5, 6, 3, 2, -4, -6]))       # 6
print(solution([-1, -1, -1, -1, 0, 1, 20, 19, 17]))                 # 20