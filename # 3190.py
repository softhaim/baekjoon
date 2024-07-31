# 3190
'''
게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
'''
import sys
from collections import deque

input = sys.stdin.readline

N = int(input()) # 보드의 크기
K = int(input()) # 사과의 개수
# 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
# 사과의 위치
apple_pos = [[False]*(N+1) for i in range(N+1) ]

for _ in range(K):
    row, column = map(int, input().split())
    apple_pos[row][column] = True

L = int(input()) # 방향 변환 횟수

snake = deque([(1,1)])
end_time = 0
game_time_list = [0]
row , column = 1, 1
up, down, right, left = False, False, True, False

def move():
    global end_time, row, column, up, down, right, left
    if right: 
        for i in range(game_time_list[-1]-game_time_list[-2]):
            column += 1
            end_time += 1
            if column > N or column < 1  or (row, column) in snake:
                print(end_time)
                sys.exit()
            if not apple_pos[row][column]:
                snake.popleft()
            else:
                apple_pos[row][column] = False
            snake.append((row, column))    
            
        if C == "D":
            down = True
            right = False
        elif C == "L":
            up = True
            right = False
    elif left:
        for i in range(game_time_list[-1]-game_time_list[-2]):
            column -= 1
            end_time += 1
            if column > N or column < 1  or (row, column) in snake:
                print(end_time)
                sys.exit()
            if not apple_pos[row][column]:
                snake.popleft()
            else:
                apple_pos[row][column] = False
            snake.append((row, column))    
        if C == "L":
            down = True
            left = False
        elif C == "D":
            up = True
            left = False
    elif up:
        for i in range(game_time_list[-1]-game_time_list[-2]):
            row -= 1
            end_time += 1
            if row > N or row < 1 or (row, column) in snake:
                print(end_time)
                sys.exit()
            if not apple_pos[row][column]:
                snake.popleft()
            else:
                apple_pos[row][column] = False
            snake.append((row, column))    
        if C == "L":
            left = True
            up = False
        elif C == "D":
            right = True
            up = False
    else:
        for i in range(game_time_list[-1]-game_time_list[-2]):
            row += 1
            end_time += 1
            if row > N or row < 1 or (row, column) in snake:
                print(end_time)
                sys.exit()
            if not apple_pos[row][column]:
                snake.popleft()
            else:
                apple_pos[row][column] = False
            snake.append((row, column))        
        if C == "L":
            right = True
            down = False
        elif C == "D":
            left = True
            down = False

for _ in range(L):
    X, C = input().split() # x초가 끝난뒤에 왼쪽, 오른쪽으로 방향 90도 회전
    game_time_list.append(int(X))
    move()
# 마지막 입력까지 받고 그 이후에 계속 초마다 이어 나가기에 한 번 더 호출
# 시간은 최대 끝에서 끝까지인 보드 크기 만큼 시간을 마지막 넣어줌 (마지막 시간 + 보드 크기)
game_time_list.append(game_time_list[-1] + N)
move()