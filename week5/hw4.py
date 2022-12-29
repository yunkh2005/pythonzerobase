def solution(N, trust):
    if N == 1:
        return 1
    
    people = [0] * N
    trusted = [0] * N
    
    for i in range(len(trust)):
        people[trust[i][0] - 1] += 1
        trusted[trust[i][1] - 1] += 1
    
    if N - 1 in trusted and 0 in people and people.index(0) == trusted.index(N - 1):
        return trusted.index(N - 1) + 1
    return -1

print(solution(2, [[1,2]]))                                 # 2
print(solution(3, [[1,3],[2,3]]))                           # 3
print(solution(3, [[1,3],[2,3],[3,1]]))                     # -1
print(solution(3, [[1,2],[2,3]]))                           # -1
print(solution(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))         # 3