import itertools
import numpy

def solution(nums, target):
    arr = list(itertools.permutations(nums, 4))
    result = []
    for i in arr:
        if sum(i) == target:
            result.append(list(i))
    
    x = numpy.sort(result, axis = 1)
    x = x.tolist()
    x = list(set([tuple(i) for i in x]))

    print_arr = numpy.array(x).reshape((3, 4))
    return print_arr

nums = [1, 0, -1, 0, -2, 2]
target = 0
print(solution(nums, target))