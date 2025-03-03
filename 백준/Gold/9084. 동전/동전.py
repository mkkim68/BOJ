import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [[1] + [0] * M for _ in range(N)]

    for j in range(1, M+1):
        if j % coins[0] == 0:
            dp[0][j] = 1
    for i in range(1, N):
        coin = coins[i]
        for j in range(1, M+1):
            if j - coin >= 0:
                dp[i][j] = dp[i][j-coin] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[-1][-1])