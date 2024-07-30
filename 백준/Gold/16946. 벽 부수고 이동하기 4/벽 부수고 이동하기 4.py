import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(N)]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def flood_fill(r, c, idx):
    q = deque()
    q.append((r, c))
    indexedMap[r][c] = idx
    total = 1
    while q:
        nowr, nowc = q.popleft()
        for dr, dc in delta:
            nr, nc = dr + nowr, dc + nowc
            if 0 <= nr < N and 0 <= nc < M and indexedMap[nr][nc] == 0 and board[nr][nc] == 0:
                indexedMap[nr][nc] = idx
                q.append((nr, nc))
                total += 1
    return total


indexedMap = [[0] * M for _ in range(N)]
idx = 1
spaces = {}
for r in range(N):
    for c in range(M):
        if indexedMap[r][c] != 0:
            continue
        if board[r][c] == 1:
            continue
        temp = flood_fill(r, c, idx)
        spaces[idx] = temp
        idx += 1

ans = [[0] * M for _ in range(N)]

for r in range(N):
    for c in range(M):
        if indexedMap[r][c] == 0:
            temp = 1
            history = set()
            for dr, dc in delta:
                nr, nc = dr + r, dc + c
                if 0 <= nr < N and 0 <= nc < M and indexedMap[nr][nc] != 0:
                    history.add(indexedMap[nr][nc])
            for num in history:
                temp += spaces[num]
            ans[r][c] = temp%10

for b in ans:
    print(*b, sep='')