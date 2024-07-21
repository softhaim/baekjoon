# 1931

import sys

N = int(sys.stdin.readline())

time = [[0]*2 for i in range(N)]
for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    time[i][0] = start
    time[i][1] = end

# 각 요소 x 를 입력으로 받고, 튜플 (x[1], x[0]) 반환
# 첫 번째 기준 정렬 (x[1]) 즉, 모든 요소는 두 번째 원소에 따라 먼저 정렬 됨
time.sort(key=lambda x:(x[1], x[0]))

count = 1
end_time = time[0][1]

for i in range(1, N):
    # 시작 시간이 끝나는 시간 보다 크면 (끝나고 나서 회의 시작 시간이면)
    if time[i][0] >= end_time:
        count += 1
        end_time = time[i][1]
        
print(count)