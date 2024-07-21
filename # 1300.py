# 1300
import sys

# N * N 행렬 만들거임
N = int(sys.stdin.readline())
# k 번째 구할거임 오름차순 했을때
k = int(sys.stdin.readline())

start, end = 1, N**2
answer = 0
# start 가 end보다 작거나 같을 때 계속 수행
'''
    우리는 이분 탐색으로 어떤 수보다 작은 자연수의 곱(i * j)이 몇 개인지 알아낼 것이다.
    A보다 작은 숫자가 몇개인지 찾아내면 A가 몇 번째 숫자인지 알 수 있다
    5으로 생각해보면 5*5 배열에서 10보다 작거나 같은 수 찾으면 
    1*1, 1*2, 1*3, 1*4, 1*5
    2*1, 2*2, 2*3, 2*4, 2*5
    3*1, 3*2, 3*3
    4*1, 4*2
    5*1, 5*2
    이렇게 되고, 여기서 나오는 패턴은 목표하는 수 k (예제에서 10으로 설정) 을 행으로 나눈 값이다.
    단, 행으로 k를 나눈 값이 행렬의 크기인 N을 초과할 수는 없다. (그로 인해 1은 10/1 인데 5개 뿐, 왜냐? 5*5였기에)
    그렇게 생각해보면 i번째 행일때, min(N, k//i) 가 될것이다.
    단 k 는 이분 탐색으로 mid로 설정하고 해당 설정 값으로 계산한 개수가 k를 넘긴다면 -> end에서 -1 해 범위 줄이기
    안넘는다면 start +1 로 범위 줄이기
''' 
while start <= end:
    mid = (start + end) // 2 
    num_of_under_mid = 0

    for i in range(1, N+1):
        num_of_under_mid += min(mid//i, N)

    if num_of_under_mid >= k:
        answer = mid
        end = mid -1
    else:
        start = mid + 1

print(answer)
