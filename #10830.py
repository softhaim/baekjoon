#10830

import sys

N, B = map(int, sys.stdin.readline().split())
mat = []
for i in range(N):  
    mat.append(list(map(int, sys.stdin.readline().split())))

def mat_mul(mat1, mat2):
    res = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            for z in range(N):
                res[i][j] += mat1[i][z] * mat2[z][j] % 1000
    return res

def divide(a, b):
    if b == 1:
        return a
    else:
        temp = divide(a,b//2)
        if b%2 == 0:
            return mat_mul(temp, temp)
        else:
            return mat_mul(mat_mul(temp, temp), a)
        
result = divide(mat, B)

# 출력
for row in result:
    for col in row:
        print(col % 1000, end=" ")
    print()