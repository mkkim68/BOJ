import sys
input = sys.stdin.readline

board = [list(map(int, list(input().strip()))) for _ in range(9)]

rows = [[0] * 10 for _ in range(9)]
cols = [[0] * 10 for _ in range(9)]
boxes = [[0] * 10 for _ in range(9)]
visited = [[0] * 9 for _ in range(9)]

def find_box(r, c):
    if r < 3:
        if c < 3:
            return 0
        elif c < 6:
            return 1
        elif c < 9:
            return 2
    elif r < 6:
        if c < 3:
            return 3
        elif c < 6:
            return 4
        elif c < 9:
            return 5
    elif r < 9:
        if c < 3:
            return 6
        elif c < 6:
            return 7
        elif c < 9:
            return 8

for r in range(9):
    for c in range(9):
        num = board[r][c]
        if num > 0:
            rows[r][num] = 1
            cols[c][num] = 1
            boxes[find_box(r, c)][num] = 1
            visited[r][c] = 1

def sol(idx):
    if idx == 81:
        for b in board:
            print(*b, sep='')
        exit()

    r, c = divmod(idx, 9)

    if visited[r][c]:
        sol(idx+1)
    else:
        for num in range(1, 10):
            bidx = find_box(r, c)
            if not rows[r][num] and not cols[c][num] and not boxes[bidx][num]:
                visited[r][c], rows[r][num], cols[c][num], boxes[bidx][num] = 1, 1, 1, 1
                board[r][c] = num
                sol(idx+1)
                visited[r][c], rows[r][num], cols[c][num], boxes[bidx][num] = 0, 0, 0, 0
                board[r][c] = 0


sol(0)
