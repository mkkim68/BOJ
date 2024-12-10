import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

jr, jc = 1000, 1000
fire_points = []
for r in range(R):
    for c in range(C):
        if board[r][c] == 'J':
            jr, jc = r, c
        elif board[r][c] == 'F':
            fire_points.append((r, c))

delta = [(1, 0), (0, 1), (0, -1), (-1, 0)]
fires = [[1e9] * C for _ in range(R)]

if fire_points:
    fire_q = deque()
    for fr, fc in fire_points:
        fires[fr][fc] = 0
        fire_q.append((fr, fc))
    while fire_q:
        r, c = fire_q.popleft()

        for dr, dc in delta:
            nr, nc = dr + r, dc + c

            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != '#':
                if fires[nr][nc] <= fires[r][c] + 1:
                    continue
                fires[nr][nc] = fires[r][c] + 1
                fire_q.append((nr, nc))


def is_exit(r, c):
    possible_cnt, wall_cnt = 0, 0
    for dr, dc in delta:
        nr, nc = dr + r, dc + c
        if 0 <= nr < R and 0 <= nc < C:
            possible_cnt += 1
            if board[nr][nc] == '#':
                wall_cnt += 1

    if possible_cnt > wall_cnt:
        return True
    return False


ans = 1e9
jh_q = deque()
jihoon = [[-1] * C for _ in range(R)]
jihoon[jr][jc] = 0
jh_q.append((jr, jc))
while jh_q:
    r, c = jh_q.popleft()

    for dr, dc in delta:
        nr, nc = dr + r, dc + c

        if (nr < 0 or nr == R) or (nc < 0 or nc == C):
            ans = min(ans, jihoon[r][c] + 1)

        if 0 <= nr < R and 0 <= nc < C and jihoon[nr][nc] == -1 and board[nr][nc] != '#':
            if fires[nr][nc] <= jihoon[r][c] + 1:
                continue
            else:
                jihoon[nr][nc] = jihoon[r][c] + 1
                jh_q.append((nr, nc))

if ans == 1e9:
    print("IMPOSSIBLE")
else:
    print(ans)

# 5 5
# #####
# #J#F#
# #.#.#
# #...#
# ##.##
