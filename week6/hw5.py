N, M, V = 4, 5, 1
edges = [[1, 2], [1, 3], [1,4], [2, 3], [3, 4]]
result = [[0] * (N + 1) for _ in range(N + 1)] 
visited = [0] * (N + 1)

def solution(N, M, V, edges):
    answer = []
    answer_str = ''
    for a, b in edges:
        result[a][b] = result[b][a] = 1
    
    def dfs(V):
        visited[V] = 1 
        answer.append(str(V))
        for i in range(1, N + 1):
            if visited[i] == 0 and result[V][i] == 1:
                dfs(i)

    dfs(V)
    answer_str = ' '.join(answer)

    return answer_str

print(solution(N, M, V, edges))