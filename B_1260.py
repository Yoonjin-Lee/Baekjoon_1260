from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * 9
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(gragh, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, v, visited)

visited = [False] * 9
print()

bfs(graph, v, visited)