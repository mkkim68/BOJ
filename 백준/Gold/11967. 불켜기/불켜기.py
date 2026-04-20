import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
switches = defaultdict(list)
for _ in range(M):
    x, y, a, b = map(int, input().split())
    switches[(x-1, y-1)].append((a-1, b-1))

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
board = [[0] * N for _ in range(N)]
board[0][0] = 1
visited = [[0] * N for _ in range(N)]

def is_reachable(sr, sc):
    for dr, dc in delta:
        nr, nc = dr+sr, dc+sc
        if  0 <= nr < N and 0 <= nc < N and visited[nr][nc]:
            return True
    return False

dq = deque()
dq.append((0, 0))
ans = 1
while dq:
    r, c = dq.popleft()
    if (r, c) in switches:
        for sr, sc in switches[(r, c)]:
            if not board[sr][sc]:
                board[sr][sc] = 1
                ans += 1

                if is_reachable(sr, sc):
                    visited[sr][sc] = 1
                    dq.append((sr, sc))

    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 1 and not visited[nr][nc]:
            dq.append((nr, nc))
            visited[nr][nc] = 1


print(ans)