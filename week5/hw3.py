import heapq

def solution(n, vertex):
    inf = float('inf')
    queue = []
    graph = [[] for i in range(n + 1)]
    distance = [inf] * (n + 1)
    answer = 0

    for i in vertex:
        a, b = i
        graph[a].append((b, 1))
        graph[b].append((a, 1))
    
    heapq.heappush(queue, (0, 1))
    distance[1] = 0
    distance[0] = 0

    while queue:
        dist, now_node = queue.pop()
        for i in graph[now_node]:
            next_dist = i[1]
            next_node = i[0]

            cost = next_dist + dist
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))

    for i in distance:
        if i == max(distance):
            answer += 1
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))        # 3