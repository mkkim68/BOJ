import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

N, M, T = map(int, input().split())
board = {}

for i in range(1, N+1):
    board[i] = deque(map(int, input().split()))

cases = [list(map(int, input().split())) for _ in range(T)]
for tc in range(T):
    x, d, k = cases[tc]

    # 번호가 x의 배수인 원판 d 방향으로 k칸 회전
    # 0: 시계(1), 1: 반시계(-1)
    n = x
    while n <= N:
        temp = board.get(n)
        if d == 0:
            temp.rotate(k)
        else:
            temp.rotate(-k)
        board[n] = temp
        n += x

    flag = False  # 인접한 같은 수가 있었는지
    total = 0
    cnt = 0
    board1 = deepcopy(board)

    for i in range(1, N+1):
        temp = board[i]
        for j in range(M):
            now = temp[j]
            next = temp[(j+1) % M]
            if now != 'x':
                total += now
                cnt += 1
                idx = i+1
                while idx <= N and now == board[idx][j]:
                    if now == board[idx][j]:
                        flag = True
                        board1[i][j] = 'x'
                        board1[idx][j] = 'x'
                    idx += 1

                if now == next:
                    flag = True
                    board1[i][j] = 'x'
                    board1[i][(j+1) % M] = 'x'

    if flag:
        board = board1
    else:
        if cnt == 0:
            break
        avg = total / cnt
        for i in range(1, N+1):
            for j in range(M):
                if board[i][j] != 'x':
                    if board[i][j] < avg:
                        board[i][j] += 1
                    elif board[i][j] > avg:
                        board[i][j] -= 1

ans = 0
for n in board:
    for m in board[n]:
        if m != 'x':
            ans += m

print(ans)