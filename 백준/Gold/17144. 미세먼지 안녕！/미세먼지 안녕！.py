import sys
from collections import deque
input = sys.stdin.readline

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
machine_up, machine_down = -1, -1


for r in range(R):
    if board[r][0] == -1:
        if machine_up == -1:
            machine_up = r
        else:
            machine_down = r


def is_range(r, c):
    if 0 <= r < R and 0 <= c < C:
        return True
    return False


def expand():
    global board
    temp = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                cnt = 0
                for dr, dc in delta:
                    nr, nc = dr + r, dc + c
                    if not is_range(nr, nc):
                        continue
                    if board[nr][nc] == -1:
                        continue
                    cnt += 1
                    temp[nr][nc] += board[r][c] // 5
                temp[r][c] += board[r][c] - (board[r][c] // 5 * cnt)
            elif board[r][c] == -1:
                temp[r][c] = -1

    board = temp
    return


def wind():
    global board
    next_state = {(machine_up, 1): 0, (machine_down, 1): 0}

    # 위쪽 부분
    for c in range(1, C):
        nc = c + 1
        if nc < C:
            next_state[(machine_up, nc)] = board[machine_up][c]
        else:
            next_state[(machine_up-1, c)] = board[machine_up][c]

    for r in range(machine_up-1, -1, -1):
        nr = r-1
        if nr >= 0:
            next_state[(nr, -1)] = board[r][-1]
        else:
            next_state[(0, -2)] = board[r][-1]

    for c in range(C-2, -1, -1):
        nc = c - 1
        if nc >= 0:
            next_state[(0, nc)] = board[0][c]
        else:
            next_state[(1, 0)] = board[0][c]

    for r in range(1, machine_up):
        nr = r + 1
        if nr < machine_up:
            next_state[(nr, 0)] = board[r][0]

    # 아래쪽 부분
    for c in range(1, C):
        nc = c + 1
        if nc < C:
            next_state[(machine_down, nc)] = board[machine_down][c]
        else:
            next_state[(machine_down+1, c)] = board[machine_down][c]

    for r in range(machine_down+1, R):
        nr = r+1
        if nr < R:
            next_state[(nr, -1)] = board[r][-1]
        else:
            next_state[(R-1, -2)] = board[r][-1]

    for c in range(C-2, -1, -1):
        nc = c - 1
        if nc >= 0:
            next_state[(R-1, nc)] = board[R-1][c]
        else:
            next_state[(R-2, 0)] = board[R-1][c]

    for r in range(R-2, machine_down, -1):
        nr = r-1
        if nr > machine_down:
            next_state[(nr, 0)] = board[r][0]

    for r, c in next_state:
        board[r][c] = next_state[(r, c)]

    return


for t in range(T):
    # 미세먼지 확산
    expand()
    # 공기청정기 작동
    wind()

ans = 0
for r in range(R):
    for c in range(C):
        if board[r][c] > 0:
            ans += board[r][c]

print(ans)