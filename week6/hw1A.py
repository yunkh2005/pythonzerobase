'''
과제 1

리스트 [1,2,3,...,n] 를 섞는 방법은 총 n! 가지이다. 
n = 3일 때 3! = 6개의 섞은 결과는 아래와 같은 순서를 가진다고 하자.
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
n과 k가 주어졌을 때, k번째 섞은 결과를 반환하시오. (단, 1 <= n <= 9, 1 <= k <= n!)

예시입력
n	k	return
3	3	[2, 1, 3]
4	9	[2, 3, 1, 4]
'''
def solution(n, k):
    fact = {0: 1}
    def factorial(num):
        if num in fact:
            return fact[num]
        val = factorial(num - 1) * num
        fact[num] = val
        return val

    remainder = k - 1
    seq = [i for i in range(1, n + 1)]
    ans = []
    for i in range(n - 1, 0, -1):
        div = factorial(i)
        val = remainder // div
        remainder %= div
        ans.append(seq[val])
        del seq[val]
    ans.append(seq[0])
    return ans

print(solution(3, 3))
print(solution(4, 9))
