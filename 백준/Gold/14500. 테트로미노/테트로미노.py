import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = set()
blocks = [
    [(0, 1), (0, 2), (0, 3)],
    [(1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 0), (1, 1)],
    [(1, 0), (2, 0), (2, 1)],
    [(1, 0), (0, 1), (0, 2)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 1), (0, 2), (-1, 2)],
    [(1, 0), (2, 0), (2, -1)],
    [(1, 0), (1, 1), (1, 2)],
    [(0, 1), (1, 0), (2, 0)],
    [(0, 1), (0, 2), (1, 2)],
    [(0, 1), (1, 1), (0, 2)],
    [(1, 0), (1, -1), (1, 1)],
    [(1, 0), (2, 0), (1, -1)],
    [(1, 0), (2, 0), (1, 1)],
    [(1, 0), (1, 1), (2, 1)],
    [(0, 1), (-1, 1), (-1, 2)],
    [(1, 0), (1, -1), (2, -1)],
    [(0, 1), (1, 1), (1, 2)]
]


ans = 0
for r in range(N):
    for c in range(M):
        for block in blocks:
            temp = board[r][c]
            for dr, dc in block:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    temp += board[nr][nc]
                else:
                    break
            else:
                ans = max(ans, temp)

print(ans)