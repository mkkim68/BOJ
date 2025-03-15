import sys
from collections import deque
input = sys.stdin.readline

N, M, G, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0
# 0: 호수, 1: 배양액 x, 2: 배양액 o

possibles = []
for r in range(N):
    for c in range(M):
        if board[r][c] == 2:
            possibles.append((r, c))


def check(garr, rarr):
    q = deque()
    used = [[(-1, '')] * M for _ in range(N)]
    cnt = 0

    for i in garr:
        r, c = possibles[i]
        used[r][c] = (0, 'G')
        q.append((r, c, 0, 'G'))
    for i in rarr:
        r, c = possibles[i]
        used[r][c] = (0, 'R')
        q.append((r, c, 0, 'R'))

    while q:
        r, c, t, color = q.popleft()
        if used[r][c] == (-2, 'F'):
            continue

        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == 0:
                    continue
                if used[nr][nc][0] == -1:
                    used[nr][nc] = (t + 1, color)
                    q.append((nr, nc, t+1, color))
                elif used[nr][nc][0] == t+1 and used[nr][nc][1] != color:
                    cnt += 1
                    used[nr][nc] = (-2, 'F')

    return cnt

P = len(possibles)
visited = [0] * P
def combi_R(idx, arr, garr):
    global ans
    if len(arr) == R:
        ans = max(ans, check(garr, arr))
        return

    for i in range(idx, P):
        if visited[i] == 0:
            visited[i] = 1
            combi_R(i+1, arr+[i], garr)
            visited[i] = 0

def combi_G(idx, arr):
    if len(arr) == G:
        combi_R(0, [], arr)
        return

    for i in range(idx, P):
        if visited[i] == 0:
            visited[i] = 1
            combi_G(i+1, arr+[i])
            visited[i] = 0

combi_G(0, [])
print(ans)