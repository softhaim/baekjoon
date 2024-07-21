# # 24479

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
    graph[i].sort()

dfs(graph, R, visited)

for i in range(1, N+1):
    print(cnt[i])

'''
아래 코드도 시간 복잡도는 O(N + M) 이지만 모든 간선을 반복문으로 검사하기 때문에 좀 비효율적
'''


# def dfs(V, E, R):
#     # 방문 딕셔너리 만들고 해당 정점의 value가 True 면 방문 한 것
#     visited[R] = True
#     visited_time_asc.append(R)

#     for tup in E:
#         if tup[0] == R: 
#             if visited[tup[1]] == False:
#                 dfs(V, E, tup[1]) 
#         elif tup[1] == R:
#             if visited[tup[0]] == False:
#                 dfs(V, E, tup[0]) 

# N, M, R = map(int, sys.stdin.readline().split())

# visited = dict()
# visited_time_asc = []

# V = set()
# E = set()

# for i in range(M):
#     u, v = map(int, sys.stdin.readline().split())
#     E.add((u, v))
#     V.add(u)
#     V.add(v)

# # 노드들 초기화
# for i in range(N):
#     visited[i] = False

# # 오름차순 방문 위한 정렬
# for i in range(len(E)):
#     sorted_E = sorted(E, key=lambda x: (x[0], x[1]))

# dfs(V, sorted_E, R)

# # for i in range(N-len(visited_time_asc)):
# #     visited_time_asc.append(0)

# for i in visited_time_asc:
#     print(i)
# for i in range(N-len(visited_time_asc)):
#     print(0)

