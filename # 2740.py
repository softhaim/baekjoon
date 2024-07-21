#2740

import sys

# 입력 처리
N, M = map(int, sys.stdin.readline().split())
A = []
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

N, M = map(int, sys.stdin.readline().split())
B = []
for i in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))

# 행렬 곱셈
def mul_matrix(mat1, mat2):
    res = [[0] * len(mat2[0]) for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for z in range(len(mat1[0])):
                res[i][j] += mat1[i][z] * mat2[z][j]
    return res

print(mul_matrix(A, B))
