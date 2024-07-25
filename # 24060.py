# 24060

import sys
# 재귀 깊이 제한 늘리기
sys.setrecursionlimit(10**6)

n, k = map(int, sys.stdin.readline().split())

array_a = list(map(int, sys.stdin.readline().split()))
save_cnt = 0

def merge_sort(array, p, r):
    if (p< r):
        mid = (p + r) // 2
        merge_sort(array, p, mid) # 전반부
        merge_sort(array, mid+1, r) # 후반부
        merge(array, p, mid, r)   # 병합

def merge(array, p, mid, r):
    global save_cnt
    i = p
    j = mid + 1
    t = 0
    tmp = []
    while(i <= mid and j <= r):
        if(array[i]<=array[j]):
            tmp.append(array[i])
            i += 1
        else:
            tmp.append(array[j])
            j += 1
    while (i<= mid): # 왼쪽 배열 부분 남은 경우
        tmp.append(array[i])
        i += 1
    while (j <= r): # 오른쪽 배열 부분 남은 경우
        tmp.append(array[j])
        j += 1
    # 결과 array에 저장 위해 i 초기화
    i = p
    while(i <= r): # 결과 array에 저장
        array[i] = tmp[t]
        save_cnt += 1
        if save_cnt == k:
            print(array[i])
            sys.exit()
        t += 1
        i += 1
        
merge_sort(array_a, 0, len(array_a)-1)
if save_cnt < k:
    print(-1)