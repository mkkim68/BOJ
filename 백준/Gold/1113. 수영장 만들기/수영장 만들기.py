import sys
from collections import deque
input = sys.stdin.readline


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(num):
    q = deque()
    board[0][0] = num
    q.append((0, 0))
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr <= N+1 and 0<=nc<=M+1 and board[nr][nc] < num:
                board[nr][nc] = num
                q.append((nr, nc))
    return


N, M = map(int, input().split())
board = [[0] * (M+2)]
maxh = 0
for _ in range(N):
    now = [0] + list(map(int, list(input().strip()))) + [0]
    maxh = max(max(now), maxh)
    board.append(now)
board.append([0] * (M+2))

ans = 0
for i in range(1, maxh+1):
    bfs(i)
    for r in range(1, N+1):
        for c in range(1, M+1):
            if board[r][c] < i:
                ans += 1
                board[r][c] += 1

print(ans)