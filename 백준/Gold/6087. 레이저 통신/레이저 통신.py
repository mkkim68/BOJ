import sys
from heapq import heappop, heappush
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

points = []
for r in range(N):
    for c in range(M):
        if board[r][c] == 'C':
            points.append((r, c))

r, c = points[0]
q = []
visited = [[[int(1e9)] * 4 for _ in range(M)] for _ in range(N)]
delta = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 우, 상, 좌, 하
visited[r][c] = [0] * 4

for i in range(4):
    dr, dc = delta[i]
    nr, nc = dr + r, dc + c
    if 0<=nr<N and 0<=nc<M and board[nr][nc] != '*':
        heappush(q, (0, 0, i, nr, nc))
        visited[nr][nc][i] = 0

while q:
    # print(q)
    flag, cnt, d, r, c = heappop(q) # flag 0: 같은방향, 1: 다른방향

    for i in range(4):
        dr, dc = delta[i]
        nr, nc = dr + r, dc + c
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != '*':
            if d == i:
                if visited[nr][nc][i] <= cnt:
                    continue
                heappush(q, (0, cnt, i, nr, nc))
                visited[nr][nc][i] = cnt
            else:
                if visited[nr][nc][i] <= cnt+1:
                    continue
                heappush(q, (1, cnt+1, i, nr, nc))
                visited[nr][nc][i] = cnt + 1

print(min(visited[points[1][0]][points[1][1]]))