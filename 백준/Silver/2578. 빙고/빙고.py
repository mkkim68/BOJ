import sys
input = sys.stdin.readline

def bingo(arr):
    isbingo = 0
    check_d1 = check_d2 = 0
    for i in range(5):
        check_row = check_col = 0
        for j in range(5):
            if arr[i][j] == 0:
                check_row += 1
            if arr[j][i] == 0:
                check_col += 1
        if arr[i][i] == 0:
            check_d1 += 1
        if arr[i][4-i] == 0:
            check_d2 += 1
        if check_col == 5:
            isbingo += 1
        if check_row == 5:
            isbingo += 1
    if check_d1 == 5:
        isbingo += 1
    if check_d2 == 5:
        isbingo += 1
    if isbingo >= 3:
        return True
    else:
        return False


board = []
announce = []
for _ in range(5):
    board.append(list(map(int, input().split())))
for _ in range(5):
    announce.extend(list(map(int, input().split())))

for n in range(len(announce)):
    for b in range(len(board)):
        if announce[n] in board[b]:
            i = board[b].index(announce[n])
            board[b][i] = 0
    if bingo(board):
        print(n+1)
        break


