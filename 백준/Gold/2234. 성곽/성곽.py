import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 1: 서, 2: 북, 4: 동, 8: 남
# 0001, 0010, 0100, 1000

delta = {1: (0, -1), 2: (-1, 0), 4: (0, 1), 8: (1, 0)}

rooms = []
room_areas = {}
room_points = {}
visited = [[-1] * M for _ in range(N)]
max_area = 0

def bfs(start, i):
    global max_area
    q = deque()
    q.append(start)
    used = set()
    temp = set()

    while q:
        r, c = q.popleft()
        used.add((r, c))

        for d in delta:
            dr, dc = delta[d]
            nr, nc = r + dr, c+ dc
            if 0 <= nr < N and 0 <= nc < M:
                if board[r][c] & d != d:
                    if visited[nr][nc] == -1:
                        q.append((nr, nc))
                        visited[nr][nc] = i
                        if (nr, nc) in temp:
                            temp.remove((nr, nc))
                else:
                    if (d == 4 or d == 8) and (nr, nc) not in used:
                        temp.add((nr, nc))

    room_areas[i] = len(used)
    max_area = max(max_area, len(used))
    room_points[i] = temp

idx = 1
for r in range(N):
    for c in range(M):
        if visited[r][c] >= 0:
            continue
        visited[r][c] = idx
        bfs((r, c), idx)
        idx += 1


max_new_area = 0
for i in range(1, idx):
    for r, c in room_points[i]:
        if visited[r][c] != i:
            max_new_area = max(max_new_area, room_areas[visited[r][c]] + room_areas[i])

print(idx-1)
print(max_area)
print(max_new_area)