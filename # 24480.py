# 24480

import sys
# 재귀 깊이 제한 늘리기
sys.setrecursionlimit(10**6)

def dfs(graph, r, visited):
    global t
    visited[r] = True
    cnt[r] = t
    t += 1
    for node in graph[r]:
        if not visited[node]:
            dfs(graph, node, visited)

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1) # 정점이 방문 했는지 여부
cnt = [0] * (N+1)         # 정점의 방문 순서
t = 1

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# [[], [4, 2], [1, 3, 4], [2, 4], [1, 2, 3], []] 이런걸 [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []] 이렇게 바꿈
for i in range(1, N+1):
    graph[i].sort(reverse=True)

dfs(graph, R, visited)

for i in range(1, N+1):
    print(cnt[i])
