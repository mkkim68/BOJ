import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

q = deque()
visited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
q.append((0, 0, 0))
visited[0][0][0] = 1
chance = 1
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    r, c, f = q.popleft()
    if r == N-1 and c == M-1:
        print(visited[r][c][f])
        break
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if board[nr][nc] == 0 and visited[nr][nc][f] == 0:
                visited[nr][nc][f] = visited[r][c][f] + 1
                q.append((nr, nc, f))
            elif board[nr][nc] == 1 and f == 0 and visited[nr][nc][1] == 0:
                visited[nr][nc][1] = visited[r][c][0] + 1
                q.append((nr, nc, 1))
else:
    print(-1)