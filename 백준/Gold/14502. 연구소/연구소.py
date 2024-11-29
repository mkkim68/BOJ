import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

blanks = []
viruses = []
for r in range(N):
    for c in range(M):
        if board[r][c] == 0:
            blanks.append((r, c))
        elif board[r][c] == 2:
            viruses.append((r, c))


B = len(blanks)
visited = [0] * B
def combi(idx, arr):
    if len(arr) == 3:
        sol(arr)
        return

    for i in range(idx, B):
        if visited[i] == 0:
            visited[i] = 1
            combi(i+1, arr + [blanks[i]])
            visited[i] = 0

def is_range(r, c):
    if 0<=r<N and 0<=c<M:
        return True
    return False


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0
def sol(new_wall):
    global ans
    new_virus = set()

    visited = [[0] * M for _ in range(N)]
    q = deque()
    for virus in viruses:
        q.append(virus)

    while q:
        r, c = q.popleft()
        if visited[r][c] == 1:
            continue

        visited[r][c] = 1
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if is_range(nr, nc) and visited[nr][nc] == 0 and (nr, nc) not in new_wall and board[nr][nc] == 0:
                new_virus.add((nr, nc))
                q.append((nr, nc))

    safe = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] == 0:
                if (r, c) not in new_wall and (r, c) not in new_virus:
                    safe += 1

    ans = max(ans, safe)
    return


combi(0, [])
print(ans)