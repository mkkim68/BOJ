import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
delta = [(1, 0), (0, -1), (-1, 0), (0, 1)]
horse = [(2, 1), (2, -1), (-2, -1), (-2, 1), (1, 2), (1, -2), (-1, -2), (-1, 2)]

visited = [[[0] * (K+1) for _ in range(W)] for j in range(H)]
q = deque()
q.append((0, 0, 0))
while q:
    r, c, h = q.popleft() # h: 말 움직임으로 몇 번 움직였는가

    if r == H-1 and c == W-1:
        ans = 1e9
        for temp in visited[r][c]:
            if temp > 0:
                ans = min(ans, temp)
        if ans < 1e9:
            print(ans)
        else:
            print(0)
        break

    for dr, dc in delta:
        nr, nc = dr + r, dc + c
        if 0 <= nr < H and 0 <= nc < W and board[nr][nc] != 1 and visited[nr][nc][h] == 0:
            q.append((nr, nc, h))
            visited[nr][nc][h] = visited[r][c][h] + 1

    if h < K:
        for dr, dc in horse:
            nr, nc = dr + r, dc + c
            if 0 <= nr < H and 0 <= nc < W and board[nr][nc] != 1 and visited[nr][nc][h+1] == 0:
                q.append((nr, nc, h+1))
                visited[nr][nc][h+1] = visited[r][c][h] + 1
else:
    print(-1)

