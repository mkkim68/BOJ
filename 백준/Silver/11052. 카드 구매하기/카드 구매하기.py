import sys
input = sys.stdin.readline

N = int(input())
arr = [0]+list(map(int, input().split()))

dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    dp[1][i] = arr[1] * i


for i in range(2, N+1):
    now = arr[i]
    for j in range(1, N+1):
        if j < i:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j-i] + now, dp[i][j-i] + now)
print(dp[-1][-1])