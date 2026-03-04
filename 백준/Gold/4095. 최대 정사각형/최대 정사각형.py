import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    board = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * M for _ in range(N)]
    dp[0] = board[0]
    ans = max(board[0])
    for i in range(N):
        if board[i][0] == 1:
            ans = 1
            dp[i][0] = 1

    for i in range(1, N):
        for j in range(1, M):
            if board[i][j] == 1:
                temp = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                dp[i][j] = temp
                ans = max(ans, temp)

    print(ans)
