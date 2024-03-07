import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 0: 청소되지 않은 칸, 1: 벽
dir = {0: (-1,0), 1:(0, 1) , 2:(1,0) , 3:(0,-1)}  # 0: 북, 1: 동, 2: 남, 3: 서
delta = deque([dir[0], dir[3], dir[2], dir[1]])  # 초기: 북,서,남,동 (반시계 -1)
while True:
    delta.rotate(1)
    if delta[0] == dir[d]:
        break

curr, curc = r, c
cnt = 0
while True:
    if room[curr][curc] == 0:
        room[curr][curc] = 99  # 청소하면 99
        cnt += 1
    temp = deepcopy(delta)
    temp.rotate(-1)
    for i in range(4):
        dr, dc = temp[i][0], temp[i][1]
        nr, nc = curr + dr, curc + dc
        if 0<=nr<N and 0<=nc<M:
            if room[nr][nc] == 0:
                curr, curc = nr, nc
                temp.rotate(-i)
                delta = deepcopy(temp)
                break
    else:
        dr, dc = delta[-2][0], delta[-2][1]
        nr, nc = curr + dr, curc + dc
        if room[nr][nc] == 1:
            break
        else:
            curr, curc = nr, nc

print(cnt)