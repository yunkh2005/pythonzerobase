def solution(intervals):
    merged = []
    for i in sorted(intervals, key = lambda x: x[0]):
        if merged and i[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], i[1])
        else:
            merged += i,
    
    return merged

print(solution([[1,3],[2,6],[8,10],[15,18]]))
# 출력: [[1,6],[8,10],[15,18]]

print(solution([[1,4],[4,5]]))
# 출력: [[1,5]]