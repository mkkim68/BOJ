import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * N for _ in range(2)]

    for i in range(2):
        dp[i][0] = stickers[i][0]

    for i in range(1, N):
        dp[0][i] = max(dp[1][i-1] + stickers[0][i], dp[0][i-1])
        dp[1][i] = max(dp[0][i-1] + stickers[1][i], dp[1][i-1])

    # for d in dp:
    #     print(d)

    print(max(dp[0][-1], dp[1][-1]))
    