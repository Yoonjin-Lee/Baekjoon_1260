n, m, v = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
