from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [False] * 9
for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, v, visited)


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


#dfs(graph, v, visited)

print(graph)

visited = [False] * 9

bfs(graph, v, visited)