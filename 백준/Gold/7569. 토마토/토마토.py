import sys
from collections import deque
input = sys.stdin.readline

delta = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
def bfs():
    global q
    while q:
        ch, cr, cc = q.popleft()
        for dh, dr, dc in delta:
            nh, nr, nc = dh + ch, dr + cr, dc + cc
            if 0<=nh<H and 0<=nr<N and 0<=nc<M and board[nh][nr][nc] == 0:
                board[nh][nr][nc] = board[ch][cr][cc] + 1
                q.append((nh, nr, nc))


M, N, H = map(int, input().split())
board = []
for _ in range(H):
    temp = []
    for _ in range(N):
        temp.append(list(map(int, input().split())))
    board.append(temp)


ans = 0
q = deque()
for h in range(H):
    for r in range(N):
        for c in range(M):
            if board[h][r][c] == 1:
                q.append((h, r, c))

bfs()
flag = 0
for temp in board:
    for row in temp:
        if 0 in row:
            print(-1)
            flag = 1
            break
        ans = max(ans, max(row))
    if flag == 1:
        break
else:
    print(ans - 1)