# 2749
'''
피보나치이다. 아마도 DP 이용하는 문제...  인줄 알았으나, 행렬을 이용한것이였음. 분할 정복 사용해 logN 으로 줄이는 것이 목표
'''
'''
import sys
input = sys.stdin.readline

import numpy as np
MOD = 1000000

def matrix_pow(mat, exp, mod):
    # 행렬 a와 B의 곱셈을 수행한다.
    result = np.eye(2, dtype=np.int64) # 단위 행렬 생성
    base = mat

    while exp > 0: # 지수가 0이 될 때까지 반복

        # 짝수일 때는 n 을 반으로 줄이고 그 결과를 제곱하면 됨.
        # 홀수일 때는 n−1은 짝수가 되므로, 한 번의 곱셈을 한 후 다시 분할 정복을 적용할 수 있음.

        if exp % 2 == 1: # exp 현재 지수가 홀수이면, 현재의 base를 결과에 곱함.
            result = np.dot(result, base) % mod # 행렬 곱셈
        base = np.dot(base, base) % mod # 매번 base를 제곱하여 지수를 절반으로 줄임
        exp //= 2 # 지수를 절반으로 나눔

    return result

def fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    # 초기 행렬 설정
    F = np.array([[1,1],[1,0]], dtype=np.int64)

    # 행렬을 N-1 제곱 
    result = matrix_pow(F, N-1, MOD)

    # 결과 행렬의 (0, 0)요소가 F(N)
    return result[0][0]


N = int(input())
print(fibo(N))
'''

'''
위 코드가 numpy 를 사용해서 하는 코드이다. 제출 시 numpy 사용이 안되어 안된다... 그래서 변경한다.
'''

import sys
input = sys.stdin.readline

MOD = 1000000

def matrix_mult(A, B, mod):
    # 행렬 A와 B의 곱셈을 수행한다.
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]]

def matrix_pow(mat, exp, mod):
    # 행렬 mat을 exp 제곱하는 함수
    result = [[1, 0], [0, 1]]  # 단위 행렬
    base = mat
    
    while exp > 0: # 지수가 0이 될 때까지 반복
        '''
        짝수일 때는 n 을 반으로 줄이고 그 결과를 제곱하면 됨.
        홀수일 때는 n−1은 짝수가 되므로, 한 번의 곱셈을 한 후 다시 분할 정복을 적용할 수 있음.
        '''
        if exp % 2 == 1:  # exp 현재 지수가 홀수이면, 현재의 base를 결과에 곱함.
            result = matrix_mult(result, base, mod)
        base = matrix_mult(base, base, mod) # 매번 base를 제곱하여 지수를 절반으로 줄임
        exp //= 2 # 지수를 절반으로 나눔
    
    return result

def fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    # 초기 행렬 설정
    F = [[1, 1], [1, 0]]
    
    # 행렬을 N-1 제곱
    result = matrix_pow(F, N - 1, MOD)
    
    # 결과 행렬의 (0, 0) 요소가 F(N)
    return result[0][0]

N = int(input())
print(fibo(N))
