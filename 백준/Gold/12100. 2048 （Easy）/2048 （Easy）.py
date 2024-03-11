import sys
from copy import deepcopy
input = sys.stdin.readline


def up(board):
    for c in range(N):
        temp = -1
        prev_r, prev_c = 99, 99
        for r in range(N):
            cur = board[r][c]
            if temp == -1:  # 맨 위
                temp = cur
                prev_r, prev_c = r, c
            elif temp == 0 and cur != 0:
                board[prev_r][prev_c] = cur
                board[r][c] = 0
                temp = cur
            elif temp == cur != 0:
                board[prev_r][prev_c] *= 2
                board[r][c] = 0
                temp = 0
                if r - prev_r > 1:
                    for r1 in range(prev_r+1, r):
                        if board[r1][c] == 0:
                            prev_r, prev_c = r1, c
                            break
                else:
                    prev_r, prev_c = r, c
            elif temp != 0 and cur != 0 and temp != cur:
                if r - prev_r > 1:
                    for r1 in range(prev_r+1, r):
                        if board[r1][c] == 0:
                            board[r1][c] = cur
                            prev_r, prev_c = r1, c
                            temp = cur
                            board[r][c] = 0
                            break
                else:
                    temp = cur
                    prev_r, prev_c = r, c
    return


def down(board):
    for c in range(N):
        temp = -1
        prev_r, prev_c = 99, 99
        for r in range(N-1, -1, -1):
            cur = board[r][c]
            if temp == -1:
                temp = cur
                prev_r, prev_c = r, c
            elif temp == 0 and cur != 0:
                board[prev_r][prev_c] = cur
                board[r][c] = 0
                temp = cur
            elif temp == cur != 0:
                board[prev_r][prev_c] *= 2
                board[r][c] = 0
                temp = 0
                if prev_r-r > 1:
                    for r1 in range(prev_r-1, r,-1):
                        if board[r1][c] == 0:
                            prev_r, prev_c = r1, c
                            break
                else:
                    prev_r, prev_c = r, c
            elif temp != 0 and cur != 0 and temp != cur:
                if prev_r - r > 1:
                    for r1 in range(prev_r-1, r, -1):
                        if board[r1][c] == 0:
                            board[r1][c] = cur
                            prev_r, prev_c = r1, c
                            temp = cur
                            board[r][c] = 0
                            break
                else:
                    temp = cur
                    prev_r, prev_c = r, c
    return


def right(board):
    for r in range(N):
        temp = -1
        prev_r, prev_c = 99, 99
        for c in range(N-1, -1, -1):
            cur = board[r][c]
            if temp == -1:
                temp = cur
                prev_r, prev_c = r, c
            elif temp == 0 and cur != 0:
                board[prev_r][prev_c] = cur
                board[r][c] = 0
                temp = cur
            elif temp == cur != 0:
                board[prev_r][prev_c] *= 2
                board[r][c] = 0
                temp = 0
                if prev_c - c > 1:
                    for c1 in range(prev_c-1, c, -1):
                        if board[r][c1] == 0:
                            prev_r, prev_c = r, c1
                            break
                else:
                    prev_r, prev_c = r, c
            elif temp != 0 and cur != 0 and temp != cur:
                if prev_c - c > 1:
                    for c1 in range(prev_c-1, c, -1):
                        if board[r][c1] == 0:
                            board[r][c1] = cur
                            prev_r, prev_c = r, c1
                            temp = cur
                            board[r][c] = 0
                            break
                else:
                    temp = cur
                    prev_r, prev_c = r, c
    return


def left(board):
    for r in range(N):
        temp = -1
        prev_r, prev_c = 99, 99
        for c in range(N):
            cur = board[r][c]
            if temp == -1:
                temp = cur
                prev_r, prev_c = r, c
            elif temp == 0 and cur != 0:
                board[prev_r][prev_c] = cur
                board[r][c] = 0
                temp = cur
            elif temp == cur != 0:
                board[prev_r][prev_c] *= 2
                board[r][c] = 0
                temp = 0
                if c - prev_c > 1:
                    for c1 in range(prev_c+1, c):
                        if board[r][c1] == 0:
                            prev_r, prev_c = r, c1
                            break
                else:
                    prev_r, prev_c = r, c
            elif temp != 0 and cur != 0 and temp != cur:
                if c - prev_c > 1:
                    for c1 in range(prev_c+1, c):
                        if board[r][c1] == 0:
                            board[r][c1] = cur
                            prev_r, prev_c = r, c1
                            temp = cur
                            board[r][c] = 0
                            break
                else:
                    temp = cur
                    prev_r, prev_c = r, c
    return


def find_max(o):
    board = deepcopy(b)
    global ans
    for command in o:
        if command == 0:  # 상
            up(board)
        elif command == 1:  # 하
            down(board)
        elif command == 2:  # 좌
            left(board)
        elif command == 3:  # 우
            right(board)
    for arr in board:
        m = max(arr)
        ans = max(m, ans)
    return


N = int(input())
b = []
for _ in range(N):
    b.append(list(map(int, input().split())))

ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            for m in range(4):
                for n in range(4):
                    order = [i, j, k, m, n]
                    find_max(order)

print(ans)