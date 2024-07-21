# 2110

import sys

N, C = map(int, sys.stdin.readline().split())

shareMeachine = []
for i in range(N):
    shareMeachine.append(int(sys.stdin.readline()))

shareMeachine.sort()
start, end = 1, shareMeachine[-1] - shareMeachine[0]

while start <= end:
    mid = (start+end)//2 # 거리
    smcount = 1
    current = shareMeachine[0] # 현재 기준 삼는 공유기
    for i in range(N):
        # 현재 공유기 사이 거리(mid) 기준으로 현재 리스트에서 거리 보다 긴 거리 위치에 설치
        if shareMeachine[i] >= current + mid:
            smcount += 1
            current = shareMeachine[i]
    # 공유기 설치 수가 목표(C)보다 크면 거리 늘림
    if smcount >= C:
        start = mid + 1
    else:
        end = mid - 1
            
print(end)