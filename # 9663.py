# 9663
import sys

## method
def sol(k): # k : 놓은 말 개수 - 점유 행 번호로도 활용 가능
    # 퀸 : 상하좌우 - x, y 좌표 확인 / 대각선 - (y=x 선상 : used_up) r+c 같으면. (y=-x 선상 : used_down) r-c같으면 놓을 수 없음.
    global n, cnt
    
    if k == n :
        cnt += 1
        return

    # i : 점유 열 번호로 활용 가능
    for i in range(n):
        if not used_column[i] and not used_up[k+i] and not used_down[(n-1)+k-i]:
            used_column[i] = True
            used_up[k+i] = True
            used_down[(n-1)+k-i] = True
            sol(k+1)
            used_column[i] = False
            used_up[k+i] = False
            used_down[(n-1)+k-i] = False

## input
n = int(input())
maps = [[0]*n for _ in range(n)]
# 열 점유 여부
used_column = [False]*n
# y = x 선상 점유 여부
used_up = [False]*(2*(n-1)+1)
# y = -x 선상 점유 여부
used_down = [False]*(2*(n-1)+1)

cnt = 0

## output
sol(0)
print(cnt)