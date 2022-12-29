import itertools

def solution(numbers):
    answer = 0
    re_arr = list(itertools.permutations(numbers, len(numbers)))
    new_arr = [0 for _ in range(len(re_arr))]

    for i in range(len(re_arr)):
        new_arr[i] = ''.join(list(map(str, re_arr[i])))

    answer = str(max(new_arr))
    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))