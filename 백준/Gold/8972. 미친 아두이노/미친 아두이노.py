import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
arr = list(map(int, input().strip()))

direcs = {
    1: (1, -1),
    2: (1, 0),
    3: (1, 1),
    4: (0, -1),
    5: (0, 0),
    6: (0, 1),
    7: (-1, -1),
    8: (-1, 0),
    9: (-1, 1)
}

sr, sc = -1, -1
a_points = []
for r in range(R):
    for c in range(C):
        if board[r][c] == 'I':
            sr, sc = r, c
        elif board[r][c] == 'R':
            a_points.append((r, c))

r, c = sr, sc
for i in range(len(arr)):
    board[r][c] = '.'
    d = arr[i]
    dr, dc = direcs[d]
    r += dr
    c += dc
    board[r][c] = 'I'

    if board[r][c] == 'R':
        print(f"kraj {i+1}")
        break

    next_points = {}
    flag = False
    for ar, ac in a_points:
        dis = 1000000
        n_point = (-1, -1)
        for j in range(1, 10):
            nr, nc = ar + direcs[j][0], ac + direcs[j][1]
            t_dis = abs(r-nr) + abs(c-nc)
            if t_dis < dis:
                dis = t_dis
                n_point = (nr, nc)
        if n_point == (r, c):
            flag = True
            break
        board[ar][ac] = '.'
        if n_point in next_points:
            next_points[n_point] += 1
            continue
        next_points[n_point] = 1

    if flag:
        print(f"kraj {i+1}")
        break

    a_points = []
    for key in next_points.keys():
        if next_points[key] > 1:
            continue
        nr, nc = key
        board[nr][nc] = 'R'
        a_points.append(key)

else:
    board[sr][sc] = '.'
    board[r][c] = 'I'

    for i in range(R):
        for j in range(C):
            print(board[i][j], end='')
        print()
