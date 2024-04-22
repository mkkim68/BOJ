import sys
from collections import deque
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def bfs1(r, c):
    q = deque()
    q.append((r, c))
    color = board[r][c]
    while q:
        cr, cc = q.popleft()
        if visited1[cr][cc] == 0:
            visited1[cr][cc] = 1
            for dr, dc in delta:
                nr, nc = dr + cr, dc + cc
                if 0<=nr<N and 0<=nc<N and visited1[nr][nc] == 0 and board[nr][nc] == color:
                    q.append((nr, nc))
    return

def bfs2(r, c):
    q = deque()
    q.append((r, c))
    color = board[r][c]
    while q:
        cr, cc = q.popleft()
        if visited2[cr][cc] == 0:
            visited2[cr][cc] = 1
            for dr, dc in delta:
                nr, nc = dr + cr, dc + cc
                if 0<=nr<N and 0<=nc<N and visited2[nr][nc] == 0:
                    if board[nr][nc] == color:
                        q.append((nr, nc))
                    elif board[nr][nc] == 'R' and color == 'G':
                        q.append((nr, nc))
                    elif board[nr][nc] == 'G' and color == 'R':
                        q.append((nr, nc))
    return


N = int(input())
board = []
for _ in range(N):
    board.append(list(input().strip()))


visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
cnt1, cnt2 = 0, 0
for r in range(N):
    for c in range(N):
        if visited1[r][c] == 0:
            bfs1(r, c)
            cnt1 += 1
        if visited2[r][c] == 0:
            bfs2(r, c)
            cnt2 += 1

print(cnt1, cnt2)