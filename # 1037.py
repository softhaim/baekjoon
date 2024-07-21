# 1037
# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

import sys

num_of_real_divisor = int(sys.stdin.readline()) # 진짜 약수의 개수

real_divisor = list(map(int, sys.stdin.readline().split()))

# N의 약수가 모두 주어진 상황에서 N을 구하는 프로그램 -> 약수들 중 가장 작은 수와 가장 큰 수를 곱하면 N을 구할 수 있다.
real_divisor.sort(reverse=True)
print(real_divisor[0]*real_divisor[-1])