import sys
from collections import deque
input = sys.stdin.readline


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(r, c):
    global visited, board, city
    q = deque()
    q.append((r, c))
    cnt = 0
    temp = 0
    cur = []
    while q:
        cr, cc = q.popleft()
        if (cr, cc) not in visited:
            visited.add((cr, cc))
            cur.append((cr, cc))
            temp += board[cr][cc]
            cnt += 1
            for dr, dc in delta:
                nr, nc = dr + cr, dc + cc
                if 0<=nr<N and 0<=nc<N and (nr, nc) not in visited and L <= abs(board[nr][nc]-board[cr][cc]) <= R:
                    q.append((nr, nc))
                    city += 1

    if cnt:
        p = temp // cnt
        for x, y in cur:
            board[x][y] = p
    return


N, L, R = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

day = 0
while True:
    city = 0
    visited = set()
    for r in range(N):
        for c in range(N):
            if (r, c) not in visited:
                bfs(r, c)

    if city == 0:
        print(day)
        break

    day += 1