# 2751 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
import sys
N = int(sys.stdin.readline())


num = list()
for i in range(N):
    num.append(int(sys.stdin.readline()))

num.sort()

for i in num:
    print(i)