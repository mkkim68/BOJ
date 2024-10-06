import sys
from collections import deque
input = sys.stdin.readline
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def is_range(nr, nc):
    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != '#':
        return True
    return False


def is_exit(nr, nc):
    if nr == -1 or nr == N and 0<=nc<M:
        return True

    if nc == -1 or nc == M and 0<=nr<N:
        return True

    return False


T = int(input())
for tc in range(T):
    M, N = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]


    fire_time = [[-1] * M for _ in range(N)]
    sg_time = [[-1] * M for _ in range(N)]

    # 시작 위치 찾기
    fires, sanggeun = deque(), deque()
    for r in range(N):
        for c in range(M):
            if board[r][c] == '@':
                sanggeun.append((r, c))
                sg_time[r][c] = 0
            elif board[r][c] == '*':
                fires.append((r, c))
                fire_time[r][c] = 0


    while fires:
        r, c = fires.popleft()
        for dr, dc in delta:
            nr, nc = dr + r, dc + c
            if is_range(nr, nc) and fire_time[nr][nc] == -1:
                fires.append((nr, nc))
                fire_time[nr][nc] = fire_time[r][c] + 1

    flag = False
    ans = 0
    while sanggeun:
        r, c = sanggeun.popleft()
        for dr, dc in delta:
            nr, nc = dr + r, dc + c
            if is_exit(nr, nc):
                flag = True
                ans = sg_time[r][c] + 1
                break
            if is_range(nr, nc) and (fire_time[nr][nc] == -1 or sg_time[r][c] + 1 < fire_time[nr][nc]) and sg_time[nr][nc] == -1:
                sanggeun.append((nr, nc))
                sg_time[nr][nc] = sg_time[r][c] + 1
        if flag:
            break

    if flag:
        print(ans)
    else:
        print('IMPOSSIBLE')

