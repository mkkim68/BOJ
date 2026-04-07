import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
shapes = [
    [(0, -1), (1, 0)],
    [(-1, 0), (0, -1)],
    [(-1, 0), (0, 1)],
    [(0, 1), (1, 0)]
]

visited = [[0] * M for _ in range(N)]
ans = 0

def sol(idx, total):
    global ans

    if idx == N * M:
        ans = max(ans, total)
        return

    r, c = divmod(idx, M)

    if visited[r][c]:
        sol(idx+1, total)
    else:
        for shape in shapes:
            r1, c1 = r + shape[0][0], c + shape[0][1]
            r2, c2 = r + shape[1][0], c + shape[1][1]

            if 0 <= r1 < N and 0 <= c1 < M and 0 <= r2 < N and 0 <= c2 < M:
                if not visited[r1][c1] and not visited[r2][c2]:
                    visited[r][c] = visited[r1][c1] = visited[r2][c2] = 1
                    temp = 2 * board[r][c] + board[r1][c1] + board[r2][c2]
                    sol(idx+1, total+temp)
                    visited[r][c] = visited[r1][c1] = visited[r2][c2] = 0

        sol(idx+1, total)

sol(0, 0)
print(ans)