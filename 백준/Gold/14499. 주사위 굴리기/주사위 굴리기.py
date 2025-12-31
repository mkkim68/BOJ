import sys
input = sys.stdin.readline

N, M, r, c, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
delta = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
coms = list(map(int, input().split()))

def to_right(num, pr, pc):  # 1
    global top, bottom, left, right
    temp = top
    top = left
    left = bottom

    if num == 0:
        bottom = right
        board[pr][pc] = bottom
    else:
        bottom = board[pr][pc]
        board[pr][pc] = 0

    right = temp

def to_left(num, pr, pc):  # 2
    global top, bottom, left, right
    temp = top
    top = right
    right = bottom

    if num == 0:
        bottom = left
        board[pr][pc] = bottom
    else:
        bottom = board[pr][pc]
        board[pr][pc] = 0
    left = temp

def to_up(num, pr, pc):  # 3
    global top, bottom, up, down
    temp = top
    top = down
    down = bottom

    if num == 0:
        bottom = up
        board[pr][pc] = bottom
    else:
        bottom = board[pr][pc]
        board[pr][pc] = 0
    up = temp


def to_down(num, pr, pc):  # 4
    global top, bottom, up, down
    temp = top
    top = up
    up = bottom

    if num == 0:
        bottom = down
        board[pr][pc] = bottom
    else:
        bottom = board[pr][pc]
        board[pr][pc] = 0
    down = temp


top, bottom, left, right, up, down = 0,0,0,0,0,0
for com in coms:
    dr, dc = delta[com]
    nr, nc = r + dr, c + dc
    if 0<=nr<N and 0<=nc<M:

        num = board[nr][nc]
        if com == 1:
            to_right(num, nr, nc)
        elif com == 2:
            to_left(num, nr, nc)
        elif com == 3:
            to_up(num, nr, nc)
        elif com == 4:
            to_down(num, nr, nc)

        r, c = nr, nc
        print(top)
