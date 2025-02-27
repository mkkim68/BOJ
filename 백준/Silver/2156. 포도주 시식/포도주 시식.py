import sys
input = sys.stdin.readline

N = int(input())
dp = [[0,0,0] for _ in range(N)]
for i in range(N):
    wine = int(input())
    if i == 0:
        dp[i][1] = wine
    else:
        dp[i][0] = max(dp[i-1])
        dp[i][1] = dp[i-1][0] + wine
        dp[i][2] = dp[i-1][1] + wine

print(max(dp[N-1]))