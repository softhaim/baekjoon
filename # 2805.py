# 2805

import sys

N, M = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))

strat, end = 1, max(tree)

while strat <= end:
    mid = (strat+end)//2
    treeHeight = 0
    for i in tree:
        if i >= mid:
            treeHeight += i - mid
    if treeHeight >= M:
        strat = mid + 1
    else:
        end = mid - 1
        
print(end)