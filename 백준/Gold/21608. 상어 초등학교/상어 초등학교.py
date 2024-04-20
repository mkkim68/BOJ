import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
students = {}
board = [[0] * N for _ in range(N)]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(N**2):
    student, *like = map(int, input().split())
    like = set(like)
    students[student] = like
    fcnt_max, ecnt_max, point = 0, 0, (1000, 1000)
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                fcnt, ecnt = 0, 0
                for dr, dc in delta:
                    fr, fc = dr + r, dc + c
                    if 0 <= fr < N and 0 <= fc < N:
                        if board[fr][fc] in like:
                            fcnt += 1
                        elif board[fr][fc] == 0:
                            ecnt += 1
                if fcnt_max < fcnt:
                    fcnt_max = fcnt
                    ecnt_max = ecnt
                    point = (r, c)
                elif fcnt_max == fcnt:
                    if ecnt > ecnt_max:
                        ecnt_max = ecnt
                        point = (r, c)
                    elif ecnt == ecnt_max:
                        point = min(point, (r, c))

    board[point[0]][point[1]] = student

    # for b in board:
    #     print(b)
    # print()

total = 0
for r in range(N):
    for c in range(N):
        now = board[r][c]
        cnt = 0
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] in students[now]:
                cnt += 1
        total += int(10 ** (cnt-1))

print(total)

