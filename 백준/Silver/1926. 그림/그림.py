import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
delta = [(-1, 0), (0, 1), (0, -1), (1, 0)]

def bfs(sr, sc):
    q = deque()
    q.append((sr, sc))
    temp = 0
    while q:
        r, c = q.popleft()
        if visited[r][c] == 1:
            continue
        visited[r][c] = 1
        temp += 1
        for dr, dc in delta:
            nr, nc = dr + r, dc + c
            if 0<=nr<N and 0<=nc<M and board[nr][nc] == 1 and visited[nr][nc] == 0:
                q.append((nr, nc))

    return temp

ans, cnt = 0, 0
for r in range(N):
    for c in range(M):
        if board[r][c] == 1 and visited[r][c] == 0:
            ans = max(bfs(r, c), ans)
            cnt += 1

print(cnt)
print(ans)