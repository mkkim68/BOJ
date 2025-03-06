import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
delta = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def bfs(start):
    global visited
    q = deque()
    q.append(start)
    while q:
        r, c = q.popleft()
        if visited[r][c]:
            continue

        visited[r][c] = 1
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] > 0 and visited[nr][nc] == 0:
                q.append((nr, nc))
    return

year = 1
while True:
    z_cnt = 0
    next_year = {}
    for r in range(N):
        for c in range(M):
            if board[r][c] > 0:
                temp = 0
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] <= 0:
                        temp += 1
                next_year[(r, c)] = max(board[r][c] - temp, 0)
            else:
                z_cnt += 1

    if z_cnt == N * M:
        print(0)
        break

    for r, c in next_year:
        board[r][c] = next_year[(r, c)]


    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] > 0 and visited[r][c] == 0:
                bfs((r, c))
                cnt += 1

    if cnt > 1:
        print(year)
        break

    year += 1

