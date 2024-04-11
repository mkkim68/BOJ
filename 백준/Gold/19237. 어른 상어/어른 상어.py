import sys
from collections import deque
input = sys.stdin.readline

N, M, k = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

position = {}
smell_set = set()
for r in range(N):
    for c in range(N):
        if board[r][c] != 0:
            position[board[r][c]] = (r, c)
            idx = board[r][c]
            board[r][c] = [idx, k]
            smell_set.add((r, c))

first = list(map(int, input().split()))
# 1위 2아래 3왼 4오
delta = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
sharks = {}
now = deque()
for i in range(1, M+1):
    up = list(map(int, input().split()))
    down = list(map(int, input().split()))
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    sharks[i] = [up, down, left, right]
    now.append((i, first[i-1]))

time = 0
while True:
    if len(sharks) == 1:
        print(time)
        break
    if time >= 1000:
        print(-1)
        break
    # 상어 냄새 1씩 감소
    for r in range(N):
        for c in range(N):
            if board[r][c] != 0 and type(board[r][c]) == list:
                idx, t = board[r][c]
                t -= 1
                if t >= 0:
                    board[r][c] = [idx, t]
                else:
                    board[r][c] = 0
                    smell_set.remove((r, c))

    p_dict = {}
    for i in range(len(now)):
        idx, d = now.popleft()  # 상어 번호, 방향
        try:
            now_dir = sharks[idx][d - 1]
            r, c = position[idx]
           # 이동쑈
            temp = deque()
            for nd in now_dir:
                dr, dc = delta[nd][0], delta[nd][1]
                nr, nc = dr + r, dc + c
                if 0<=nr<N and 0<=nc<N:
                    if (nr, nc) in smell_set and board[nr][nc][0] == idx:
                        temp.append((nr, nc, nd))
                    elif (nr, nc) not in smell_set:
                        now.append((idx, nd))
                        position[idx] = (nr, nc)
                        if (nr, nc) not in p_dict:
                            p_dict[(nr, nc)] = [idx]
                        else:
                            p_dict[(nr, nc)].append(idx)
                        break
            else:
                nr, nc, nd = temp.popleft()
                now.append((idx, nd))
                position[idx] = (nr, nc)
                if (nr, nc) not in p_dict:
                    p_dict[(nr, nc)] = [idx]
                else:
                    p_dict[(nr, nc)].append(idx)
        except:
            continue

    # 같은 좌표면 상어 나가기
    for key in p_dict:
        if len(p_dict[key]) >= 2:
            p_dict[key].sort()
            for idx in p_dict[key][1:]:
                del sharks[idx]
                del position[idx]

    # 상어 냄새 뿌리기
    for idx, nd in now:
        if idx in sharks:
            r, c = position[idx]
            board[r][c] = [idx, k]
            smell_set.add((r, c))

    time += 1
