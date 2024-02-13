
M = int(input())
board = [[0] * 6 for i in range(6)]
board[6//2-1][6//2-1], board[6//2][6//2] = 2, 2
board[6//2-1][6//2], board[6//2][6//2-1] = 1, 1
# 1: 흑돌, 2: 백돌
# print(board)
dj = [0, 1, 0, -1, 1, 1, -1, -1]
di = [1, 0, -1, 0, 1, -1, 1, -1]
for m in range(M):
    x, y = map(int, input().split())
    if m % 2 == 0:
        color = 1
    else:
        color = 2
    board[x-1][y-1] = color
    for drow, dcol in zip(dj, di):
        nrow, ncol = x + drow-1, y + dcol-1
        if 0 <= nrow+drow < 6 and 0 <= ncol+dcol < 6:
            if color == 1 and board[nrow][ncol] == 2:
                nx, ny = nrow + drow, ncol + dcol
                while 0 <= nx < 6 and 0 <= ny < 6:
                    if board[nx][ny] == 1:
                        if drow == 0 and dcol != 0:
                            for j in range(ncol, ny, dcol):
                                board[nrow][j] = 1
                        elif drow != 0 and dcol != 0:
                            i, j = nrow, ncol
                            while i != nx and j != ny:
                                board[i][j] = 1
                                i += drow
                                j += dcol
                        elif drow != 0 and dcol == 0:
                            for i in range(nrow, nx,drow):
                                board[i][ncol] = 1
                        break
                    elif board[nx][ny] == 0:
                        break
                    elif board[nx][ny] == 2:
                        nx += drow
                        ny += dcol
            elif color == 2 and board[nrow][ncol] == 1:
                nx, ny = nrow + drow, ncol + dcol
                while 0 <= nx < 6 and 0 <= ny < 6:
                    if board[nx][ny] == 2:
                        if drow == 0 and dcol != 0:
                            for j in range(ncol, ny, dcol):
                                board[nrow][j] = 2
                        elif drow != 0 and dcol != 0:
                            i, j = nrow, ncol
                            while i != nx and j != ny:
                                board[i][j] = 2
                                i += drow
                                j += dcol
                        elif drow != 0 and dcol == 0:
                            for i in range(nrow, nx, drow):
                                board[i][ncol] = 2
                        break
                    elif board[nx][ny] == 0:
                        break
                    elif board[nx][ny] == 1:
                        nx += drow
                        ny += dcol


black = white = 0
for i in range(6):
    for j in range(6):
        if board[i][j] == 1:
            black += 1
            board[i][j] = 'B'
        elif board[i][j] == 2:
            white += 1
            board[i][j] = 'W'
        elif board[i][j] == 0:
            board[i][j] = '.'

for i in board:
    print(*i, sep='', end='\n')
if black > white:
    print('Black')
else:
    print('White')