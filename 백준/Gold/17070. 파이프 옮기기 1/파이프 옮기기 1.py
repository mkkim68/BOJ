import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
delta = [(0, 1), (1, 0), (1, 1)] # 가로, 세로, 대각선

dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1
for r in range(N):
    for c in range(N):
        for d in range(3):
            temp = 0
            for i in range(3):
                dr, dc = delta[i]
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and not board[nr][nc]:
                    temp += 1
                else:
                    continue
                if d == 0 and i == 1:
                    continue
                elif d == 1 and i == 0:
                    continue
                if i < 2 or (i == 2 and temp == 3):
                    dp[nr][nc][i] += dp[r][c][d]

print(sum(dp[N-1][N-1]))


