#1654

import sys

K, N  = map(int, sys.stdin.readline().split())
input = []
for i in range(K):
    input.append(int(sys.stdin.readline()))

start, end = 1, max(input) # 이분 탐색 처음과 끝
while start <= end:
    mid = (start + end)//2
    lines = 0 # 랜선 수
    for i in input:
        lines += i // mid
    if lines >= N:
        start = mid + 1
    else:
        end = mid -1
        
print(end)

