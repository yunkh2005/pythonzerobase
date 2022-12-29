'''
과제 3.
N개의 문자열로 이루어진 List에서 전체 문자열이 앞 n개 문자열이 같다고 할때, 
가장 큰 n을 출력하는 알고리즘을 구현하라. 
(즉, 주어진 모든 문자열의 앞의 몇개의 문자가 일치하는지 출력하라)

def solution(a):
    return 0

# Test code
print(solution(['abcd', 'abce', 'abchg', 'abcfwqw', 'abcdfg'])) # 3
print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg'])) # 0
'''

def solution(a):
    count = 0
    w = a[0]
    for idx, c in enumerate(w):
        is_match = True
        for w_ in a:
            if c != w_[idx]:
                is_match = False
                break
        if is_match is True:
            count += 1
        else:
            break
    return count

print(solution(['abcd', 'abce', 'abchg', 'abcfwqw', 'abcdfg'])) # 3
print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg'])) # 0