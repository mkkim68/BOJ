import sys
from collections import deque
input = sys.stdin.readline
delta = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def bfs(s):
    q = deque()
    q.append(s)
    visited = [[[-1] * C for r in range(R)] for l in range(L)]
    visited[s[0]][s[1]][s[2]] = 0

    while q:
        l, r, c = q.popleft()
        if board[l][r][c] == 'E':
            return visited[l][r][c]

        for dl, dr, dc in delta:
            nl, nr, nc = dl + l, dr + r, dc + c
            if 0<=nl<L and 0<=nr<R and 0<=nc<C and visited[nl][nr][nc] == -1 and board[nl][nr][nc] != '#':
                visited[nl][nr][nc] = visited[l][r][c] + 1

                q.append((nl, nr, nc))

    return -99

while True:
    L, R, C = map(int, input().split())

    if L == R == C == 0:
        break

    board = []
    for l in range(L):
        now = [list(input().strip()) for _ in range(R)]
        input()
        board.append(now)

    flag = False
    for i in range(L):
        for r in range(R):
            for c in range(C):
                if board[i][r][c] == 'S':
                    start = (i, r, c)
                    flag = True
                    break
            if flag:
                break
        if flag:
            break

    ans = bfs(start)
    if ans == -99:
        print("Trapped!")
    else:
        print(f"Escaped in {ans} minute(s).")