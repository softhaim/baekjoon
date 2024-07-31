# 11066

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    # 편의상 1부터 시작 하기 위해 [0] 추가
    file_cost = [0] + list(map(int, input().split()))
    # dp[i][j]는 i번째 파일부터 j번째 파일을 합치는 최소값
    dp = [[0]*(k+1) for j in range(k+1)]

    # 연속합 (a부터 b까지의 부분연속합을 구할 때, b까지합 - (a-1)까지합 으로 구해주면 됨)
    # 여러번 sum함수 안써도 되고, 딕셔너리 구해두면 O(1) 연산으로 그때그때 부분합 구해서 쓰는게 효율적
    subSum = {0: 0}
    for idx in range(1, k+1):
        subSum[idx] = subSum[idx-1] + file_cost[idx]

    # 먼저dp[i][i+1]을 구함 -> 즉, 두 파일이 연속으로 되어있을 때의 합을 구하는 경우만 dp에 저장해둠
    for i in range(1, k+1):
        for j in range(1, k+1):
            if j == i+1:
                dp[i][j] = file_cost[i] + file_cost[j]

    # dp의 맨 밑에서 위로 올라오면서 dp 채워 나감
    # dp[1][4]는 dp[1][1]+dp[2][4], dp[1][2]+dp[3][4], dp[1][3]+dp[4][4]와 같은 경우의 수를 가짐
    # 만약 k가 4라면 i=3 부터 시작해서 dp[3][4] 채우고 그다음 i=2로 dp[2][4] 그다음 i=1 dp[1][3] dp[1][4]
    for i in range(k-1, 0, -1):
        for j in range(1, k+1):
            # 0이거나 자기 자신 아닌 경우(j가 작은건 존재 안함)
            if dp[i][j] == 0 and j>i:
                # i부터 j까지 합과(합친 파일의 크기) i와 j 사이의 수에서 합칠 수 있는 경우의 수의 코스트 최솟값(임시파일)을 더함 ps.그냥 sum하니까 시간초과나길래 미리 구해두고 사용
                #dp[i][j] = min([dp[i][k]+dp[k+1][j] for k in range(i,j)]) + sum(file_cost[i:j+1])
                # sum 부분을 저장해둔거로 하고 i부터 j까지의 합은 j-(i-1) 이므로 저렇게
                dp[i][j] = min([dp[i][k]+dp[k+1][j] for k in range(i,j)]) + (subSum[j] - subSum[i-1])
    print(dp[1][k])


