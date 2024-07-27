import sys

def dfs(last_num):
    if len(sequence) == m:
        print(' '.join(map(str, sequence)))
        return
    for i in range(1, n+1):
        if visit[i]:
            continue
        else:
            if i < last_num:
                continue
            #visit[i] = True
            sequence.append(i)
            dfs(i)
            sequence.pop()
            # print(sequence)
            # print(visit)  
            #visit[i] = False




n, m = map(int, sys.stdin.readline().split())

# 1 부터 n까지 자연수 중에서 중복 없이 m개를 고른 수열
# 백트랙킹 모든 경우의 수 전부 고려 하는 알고리즘
sequence = []
visit = [False]*(n+1)

dfs(0)