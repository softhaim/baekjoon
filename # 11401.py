# 11401

import sys

N, K = map(int, sys.stdin.readline().split())

def power(n, k):
    if k == 1:
        return n
    else:
        tmp = power(n, k//2)
        if k % 2 == 0:
            return tmp*tmp % 1000000007
        else:
            return tmp*tmp*n%1000000007

def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % 1000000007
    return n

def binomial_coe(n, k):
    res = factorial(n)/(factorial(k)*factorial(n-k))
    return res % 1000000007

A = factorial(N)
B = (factorial(N-K) * factorial(K)) % 1000000007

# (A/B) % p
# = A * B^-1 % p
# = A * B^-1 * B^p-1 % p
# = A * B^p-2 % p
# = (A % p) * (B^p-2 % p) % p
print((A % 1000000007) * (power(B, 1000000007-2) % 1000000007) % 1000000007 )