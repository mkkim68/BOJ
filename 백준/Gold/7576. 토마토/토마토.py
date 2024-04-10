import sys
from collections import deque
input = sys.stdin.readline


delta = [(0,1), (0,-1), (1,0), (-1,0)]
def bfs():
    global q
    while q:
        cr, cc = q.popleft()
        for dr, dc in delta:
            nr, nc = dr + cr, dc + cc
            if 0<=nr<N and 0<=nc<M and board[nr][nc] == 0:
                board[nr][nc] = board[cr][cc] + 1
                q.append((nr, nc))


M, N = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

ans = 0
q = deque()
for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            q.append((r, c))

bfs()
for b in board:
    if 0 in b:
        print(-1)
        break
    ans = max(ans, max(b))
else:
    print(ans - 1)