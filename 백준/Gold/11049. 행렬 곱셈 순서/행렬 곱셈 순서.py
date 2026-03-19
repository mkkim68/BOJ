import sys
input = sys.stdin.readline

N = int(input())
matrixs = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
for cnt in range(N-1):
    for i in range(N-1-cnt):
        j = i + cnt + 1
        dp[i][j] = 2 ** 31
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrixs[i][0]*matrixs[k][1]*matrixs[j][1])

print(dp[0][-1])