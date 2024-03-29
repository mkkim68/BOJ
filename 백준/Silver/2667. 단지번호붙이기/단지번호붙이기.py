import sys
input = sys.stdin.readline


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dfs(start):
    stack = [start]
    house = 0
    while stack:
        cr, cc = stack.pop()
        if visited[cr][cc] == 0:
            visited[cr][cc] = 1
            house += 1
            for dr, dc in delta:
                nr, nc = dr + cr, dc + cc
                if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0 and board[nr][nc] == '1':
                    stack.append((nr, nc))
    return house



N = int(input())
board = []
for _ in range(N):
    board.append(list(input().strip()))

visited = [[0] * N for _ in range(N)]

cnt = 0
h = []
for r in range(N):
    for c in range(N):
        if board[r][c] == '1' and visited[r][c] == 0:
            a = dfs((r, c))
            cnt += 1
            h.append(a)

h.sort()
print(cnt)
print(*h, sep='\n')