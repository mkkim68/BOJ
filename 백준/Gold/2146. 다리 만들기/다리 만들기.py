import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
delta = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def is_range(point):
    if 0 <= point[0] < N and 0 <= point[1] < N:
        return True
    return False

def bfs(start):
    global visited
    q = deque()
    q.append(start)
    points = []
    while q:
        r, c = q.popleft()
        if visited[r][c]:
            continue
        visited[r][c] = 1
        temp = 0
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if not is_range((nr, nc)):
                temp += 1
                continue
            if visited[nr][nc]:
                temp += 1
                continue
            if board[nr][nc]:
                q.append((nr, nc))
                temp += 1
        if temp < 4:
            points.append((r, c))
    points.sort()
    return points

visited = [[0] * N for _ in range(N)]
islands = {}
cnt = 1
for r in range(N):
    for c in range(N):
        if board[r][c] == 1 and visited[r][c] == 0:
            islands[cnt] = bfs((r, c))
            cnt += 1

ans = 1e9
for i in range(1, cnt-1):
    for j in range(i+1, cnt):
        for r, c in islands[i]:
            for nr, nc in islands[j]:
                ans = min(ans, abs(r-nr) + abs(c-nc) - 1)

print(ans)