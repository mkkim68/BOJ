import sys
from collections import deque
input = sys.stdin.readline

board = [list(input().strip()) for _ in range(12)]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(color, start):
    q = deque()
    q.append(start)
    used = []
    while q:
        r, c = q.popleft()
        used.append((r, c))
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 12 and 0 <= nc < 6 and board[nr][nc] == color and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))

    if len(used) >= 4:
        return used
    return []

cnt = 0
while True:
    visited = [[0] * 6 for _ in range(12)]
    flag = False
    for i in range(11, -1, -1):
        for j in range(6):
            if board[i][j] != '.' and not visited[i][j]:
                visited[i][j] = 1
                temp = bfs(board[i][j], (i, j))
                if temp:
                    flag = True
                    for r, c in temp:
                        board[r][c] = '.'


    if not flag:
        break

    for j in range(6):
        blanks = 0
        points = []
        for i in range(12):
            if board[i][j] != '.':
                if blanks:
                    t_points = []
                    for r, c in reversed(sorted(points)):
                        board[r + blanks][c] = board[r][c]
                        board[r][c] = '.'
                        t_points.append((r+blanks, c))
                    points = t_points
                points.append((i, j))
                blanks = 0

            else:
                blanks += 1
        if blanks:
            for r, c in reversed(sorted(points)):
                board[r+blanks][c] = board[r][c]
                board[r][c] = '.'

    cnt += 1

print(cnt)
