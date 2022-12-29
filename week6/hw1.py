import itertools

def solution(n, k):
    arr = [i for i in range(1, n + 1)]
    result = list(itertools.permutations(arr, n))

    return list(result[k - 1])

print(solution(3, 3))
print(solution(4, 9))