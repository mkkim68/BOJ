import sys
input = sys.stdin.readline

delta = [(0, 1), (1, 0), (1, 1), (1, -1)]
def dfs(start, word):
    stack = [(start, 1, -99)]
    while stack:
        now, cnt, delta_num = stack.pop()
        if cnt == 3:
            return word

        if delta_num == -99:
            for i in range(4):
                dr, dc = delta[i]
                nr, nc = dr + now[0], dc + now[1]
                if 0 <= nr < 3 and 0 <= nc < 3 and board[nr][nc] == word:
                    stack.append(((nr, nc), cnt + 1, i))
        else:
            dr, dc = delta[delta_num]
            nr, nc = dr + now[0], dc + now[1]
            if 0 <= nr < 3 and 0 <= nc < 3 and board[nr][nc] == word:
                stack.append(((nr, nc), cnt + 1, delta_num))

    return False

while True:
    tc = input().strip()
    if tc == 'end':
        break

    board = [list(tc[0:3]),list(tc[3:6]),list(tc[6:])]
    # for b in board:
    #     print(b)

    O_cnt, X_cnt = tc.count('O'), tc.count('X')

    if O_cnt > X_cnt:
        print('invalid')
        continue

    if X_cnt > O_cnt + 1:
        print('invalid')
        continue


    flag = False
    while_control = False
    for r in range(3):
        for c in range(3):
            if board[r][c] != '.':
                temp = dfs((r, c), board[r][c])
                if temp:
                    if not flag:
                        flag = board[r][c]
                    else:
                        if temp != flag:
                            print('invalid')
                            while_control = True
                            break
        if while_control:
            break
    if while_control:
        continue
    # print(flag)
    if flag == 'O':
        if X_cnt == O_cnt + 1:
            print('invalid')
            continue
    elif flag == 'X':
        if X_cnt == O_cnt:
            print('invalid')
            continue
    else:
        if X_cnt + O_cnt == 9:
            print('valid')
            continue
        print('invalid')
        continue

    print('valid')