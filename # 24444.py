# 24444

import sys
from queue import Queue

def bfs(graph, r, visited):
    global t
    visited[r] = True
    cnt[r] = t
    t += 1
    queue_order.put(r)
    while(queue_order.qsize() > 0):
        u = queue_order.get()
        for node in graph[u]:
            if not visited[node]:
                visited[node] = True
                cnt[node] = t
                t += 1
                queue_order.put(node)


N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1) # 정점이 방문 했는지 여부
cnt = [0] * (N+1)         # 정점의 방문 순서
queue_order = Queue()
t = 1

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# [[], [4, 2], [1, 3, 4], [2, 4], [1, 2, 3], []] 이런걸 [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []] 이렇게 바꿈
for i in range(1, N+1):
    graph[i].sort(reverse=True)

bfs(graph, R, visited)

for i in range(1, N+1):
    print(cnt[i])
