import sys
read = sys.stdin.readline

n, m, v = 4, 5, 1
edges = [[1, 2], [1, 3], [1,4], [2, 3], [3, 4]]
result = [[0] * (n + 1) for _ in range(n + 1)] 
visit_list = [0] * (n + 1)

for a, b in edges:
	print(a, b)
	result[a][b] = result[b][a] = 1

print(result)
