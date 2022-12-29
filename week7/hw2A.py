'''
과제 2

여러 개의 구간이 리스트 intervals로 주어졌을 때, 
겹치는 구간을 모두 병합하여 출력하시오.

입력 예시1
입력: intervals = [[1,3],[2,6],[8,10],[15,18]]
출력: [[1,6],[8,10],[15,18]]
설명: 구간 [1,3]와 [2,6]이 겹치므로, [1,6]으로 병합하였다.

입력 예시 2
입력: intervals = [[1,4],[4,5]]
출력: [[1,5]]
설명: 구간 [1,4]와 [4,5]는 겹치는 것으로 간주한다.
'''

def solution(intervals):
    intervals.sort()

    def merge(x):
        if len(x) <= 1:
            return x

        to_merge = [x[0]]
        del x[0]
        while len(x) > 0:
            if to_merge[0][1] >= x[0][0]:
                to_merge.append(x[0])
                del x[0]
            else:
                break

        merged = [to_merge[0][0], max(map(lambda e: e[1], to_merge))]
        return [merged] + merge(x)

    return merge(intervals)

print(solution([[1,3],[2,6],[8,10],[15,18]]))
# 출력: [[1,6],[8,10],[15,18]]

print(solution([[1,4],[4,5]]))
# 출력: [[1,5]]