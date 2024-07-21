#11053

import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

from bisect import bisect_left

def lis(arr):
    if not arr:
        return 0

    # lis_ends는 각 길이의 부분 수열 중 최소 끝 값들을 저장
    lis_ends = []
    
    for value in arr:
        # value가 들어갈 위치를 이진 검색으로 찾기
        pos = bisect_left(lis_ends, value)
        
        # pos가 lis_ends의 길이와 같다면 새로운 길이의 부분 수열 가능
        if pos == len(lis_ends):
            lis_ends.append(value)
        else:
            # 현재 길이의 부분 수열 중 최소 끝 값을 value로 갱신
            lis_ends[pos] = value

    return len(lis_ends)

print(lis(A))  # 출력: 4
