import sys
from collections import deque
input = sys.stdin.readline


delta = [(1,0), (-1,0), (0,1), (0,-1)]
def find():
    q = deque()
    visited = set()
    cheese = dict()
    q.append((0, 0))
    while q:
        r, c = q.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        for dr, dc in delta:
            nr, nc = dr + r, dc + c
            if 0<=nr<N and 0<=nc<M and (nr, nc) not in visited:
                if board[nr][nc] == '1':
                    if (nr, nc) not in cheese:
                        cheese[(nr, nc)] = 1
                    else:
                        cheese[(nr, nc)] += 1
                else:
                    q.append((nr, nc))

    return cheese


N, M = map(int, input().split())
board = [list(input().split()) for _ in range(N)]

ans = 0
temp = find()
while temp:
    for r, c in temp:
        if temp[(r, c)] >= 2:
            board[r][c] = ans + 1
    temp = find()
    ans += 1

print(ans)