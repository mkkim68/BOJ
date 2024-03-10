import sys
from collections import deque
input = sys.stdin.readline


def bfs(row, col, d):
    q = deque()
    q.append(deque([(row, col)]))
    while q:
        cur_d = q.popleft()
        temp = deque()
        for cur in cur_d:
            curr, curc = cur[0], cur[1]
            if visited[curr][curc] == 0:
                visited[curr][curc] = 1
                board[curr][curc] = d
                for dr, dc in delta:
                    nr, nc = curr + dr, curc + dc
                    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != '0' and visited[nr][nc] == 0:
                        temp.append((nr, nc))
        if temp:
            q.append(temp)
            d += 1


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input().split())

delta = [(-1,0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
for r in range(N):
    for c in range(M):
        if board[r][c] == '2':
            sr, sc = r, c
            break

visited = [[0] * M for i in range(N)]
bfs(sr, sc, 0)
for r in range(N):
    for c in range(M):
        if board[r][c] == '1':
            board[r][c] = -1

for b in board:
    print(*b)
