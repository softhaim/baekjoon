# 11659

import sys

N, M = map(int, sys.stdin.readline().split())

input = list(map(int, sys.stdin.readline().split()))

temp = 0
prefix_sum = [0]
for i in input:
    temp += i
    prefix_sum.append(temp)
    
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(prefix_sum[b] - prefix_sum[a-1])