import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

start = (0, 0)
dp = [[-1] * M for _ in range(N)]

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def find(now):
    r, c = now

    if r == N-1 and c == M-1:
        return 1

    if dp[r][c] != -1:
        return dp[r][c]

    ways = 0
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if board[r][c] - board[nr][nc] > 0:  # 내리막일 때
                ways += find((nr, nc))
    dp[r][c] = ways
    return dp[r][c]


print(find(start))