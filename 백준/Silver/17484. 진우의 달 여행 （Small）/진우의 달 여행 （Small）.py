import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * 3 for _ in range(M)] for _ in range(N)]
for i in range(M):
    dp[0][i] = [board[0][i]] * 3

for i in range(1, N):
    for j in range(M):
        now = board[i][j]
        if j == 0:
            for k in range(2):
                if k == 0:
                    dp[i][j][k] = now + min(dp[i-1][j+1][1:])
                else:
                    dp[i][j][k] = now + dp[i-1][j][0]
        elif j == M-1:
            for k in range(1, 3):
                if k == 2:
                    dp[i][j][k] = now + min(dp[i-1][j-1][:2])
                else:
                    dp[i][j][k] = now + dp[i-1][j][2]
        else:
            for k in range(3):
                if k == 0:
                    dp[i][j][k] = now + min(dp[i-1][j+1][1:])
                elif k == 1:
                    dp[i][j][k] = now + min(dp[i-1][j][0], dp[i-1][j][2])
                else:
                    dp[i][j][k] = now + min(dp[i-1][j-1][:2])


ans = 1e9
for j in range(M):
    if j == 0:
        ans = min(ans, min(dp[-1][j][:2]))
    elif j == M-1:
        ans = min(ans, min(dp[-1][j][1:]))
    else:
        ans = min(ans, min(dp[-1][j]))

print(ans)