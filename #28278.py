#28278번
import sys

N = int(sys.stdin.readline())
stack = list()

for i in range(N):
    input_command= sys.stdin.readline().strip()
    command = list(map(int, input_command.split()))

    if(command[0] == 1):
        stack.append(command[1])
    if(command[0] == 2):
        if stack:
            print(stack.pop())
        else:
            print("-1")
    if(command[0] == 3):
        print(len(stack))
    if(command[0] == 4):
        if stack:
            print(0)
        else:
            print("1")
    if(command[0] == 5):
        if stack:
            print(stack[-1])
        else:
            print("-1")