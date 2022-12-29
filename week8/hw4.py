def solution(N, K1, K2, W, V):
    data = []
    answer = 0
    capacity = K1 + K2

    for i in range(N):
        data.append([W[i], V[i]])
    
    data = sorted(data, key=lambda x: x[1] / x[0], reverse=True)

    for dt in data:
        if capacity - dt[0] >= 0:
            capacity -= dt[0]
            answer += dt[1]
        else:
            fraction = capacity // dt[0]
            answer += dt[1] * fraction
            break

    return answer

print(solution(4, 3, 8, [1, 5, 6, 3], [5, 2, 14, 6]))   # 25