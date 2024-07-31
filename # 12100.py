# 12100

import sys, copy

input = sys.stdin.readline

N = int(input())
board = [[0]*(N+1) for _ in range(N+1)]
row, column = 1, 1
ans = 0

for _ in range(N):
    input_init_state = list(map(int, input().split()))
    for i in input_init_state:
        board[row][column] = i
        column += 1
    column = 1
    row += 1

def left(board):
    for i in range(1, N+1):
        cursor = 1
        for j in range(2, N+1):
            if board[i][j] != 0: # 비어 있지 않으면
                tmp = board[i][j]
                board[i][j] = 0 # 왼쪽으로 옮기며 비워질거라 0으로 변경
 
                if board[i][cursor] == 0: # 옮기려는 곳의 위치의 값이 0이면(비어있으면)
                    board[i][cursor] = tmp # 그냥 옮김
                elif board[i][cursor] == tmp: # 값이 같으면
                    board[i][cursor] = 2*tmp # 합쳐진 값으로 넣음
                    cursor += 1 # 합쳐졌으니 해당 부분은 더이상 합쳐지지 않음 그렇기에 옮기는 곳은 다음곳이므로 이동
                else: # 값이 다른 경우
                    cursor += 1 # 옮겨야 하는 위치를 바로 옆으로 지정해 옆에 위치하도록 함
                    board[i][cursor] = tmp
    return board

def right(board):
    for i in range(1, N+1):
        cursor = N
        for j in range(N-1, 0, -1):
            if board[i][j] != 0: # 비어있지 않으면
                tmp = board[i][j]
                board[i][j] = 0 # 오른쪽으로 옮기며 비워질거라 0으로 변경

                if board[i][cursor] == 0: # 옮기려는 위치 값이 비었으면
                    board[i][cursor] = tmp
                elif board[i][cursor] == tmp: # 값 같으면
                    board[i][cursor] = 2*tmp
                    cursor -= 1
                else:
                    cursor -= 1
                    board[i][cursor] = tmp
            
    return board

def up(board):
    for j in range(1, N+1):
        cursor = 1
        for i in range(2, N+1):
            if board[i][j] != 0: # 비어있으면
                tmp = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = tmp
                elif board[cursor][j] == tmp:
                    board[cursor][j] = 2*tmp
                    cursor += 1
                else:
                    cursor += 1
                    board[cursor][j] = tmp
    return board
def down(board):
    for j in range(1, N+1):
        cursor = N
        for i in range(N-1, 0, -1):
            if board[i][j] != 0: # 비어있으면
                tmp = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = tmp
                elif board[cursor][j] == tmp:
                    board[cursor][j] = 2*tmp
                    cursor -= 1
                else:
                    cursor -= 1
                    board[cursor][j] = tmp
    return board

def dfs(n, arr):
    global ans
    if n == 5:
        for i in range(1, N+1):
            for j in range(1, N+1):
                if arr[i][j] > ans:
                    ans = arr[i][j]
        return
    for i in range(4):
        # 보드를 경우의 수마다 따질건데 그냥 가져다 쓰면 다음 경우에 수 계산시에 이미 변경된 거로 경우의 수를 계산하게 되기에 변경되기 전꺼로 사용하기 위해 복사
        copy_arr = copy.deepcopy(arr)
        if i == 0:
            dfs(n+1, left(copy_arr))
        elif i == 1:
            dfs(n+1, right(copy_arr))
        elif i == 2:
            dfs(n+1, up(copy_arr))
        else:
            dfs(n+1, down(copy_arr))

dfs(0, board)
print(ans)