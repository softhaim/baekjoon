# 1629
# 자연수 A를 B번 곱한 수를 알고 싶다.
# 단 구하려는 수가 매우 커질 수 있으므로 
# 이를 C로 나눈 나머지를 구하는 프로그램을 작성
import sys

A, B, C = map(int, sys.stdin.readline().split())

# 분할 정복으로 찾기
def divide(a, b):
    if b == 1:
        return a%C
    else:
        tmp = divide(a, b//2) # a^(b//2)
        if b%2 == 0:
            return tmp*tmp%C
        else:
            return tmp*tmp*a%C
        
print(divide(A,B))