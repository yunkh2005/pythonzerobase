import heapq

inf = float('inf')
n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
graph = [[] for i in range(n + 1)]
dt = [inf] * (n + 1)

print(dt)
for i in vertex:
    a, b = i
    