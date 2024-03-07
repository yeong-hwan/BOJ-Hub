import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
hostility_pairs = [tuple(map(int, input().split())) for _ in range(M)]

def dfs(start, visited, graph, group):
    visited[start] = group

    for v in graph[start]:
        if visited[v] == 0: 
            result = dfs(v, visited, graph, -group)
            if not result:
                return False
        else:
            if visited[v] == group: 
                return False
    return True

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

while hostility_pairs:
    a, b = hostility_pairs.pop()
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    if visited[i] == 0:
        result = (dfs(i, visited, graph, 1))
        if not result:
            break

print(1) if result else print(0)