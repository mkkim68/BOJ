from collections import deque
from copy import deepcopy

magnetics = {}
for i in range(1, 5):
    mag = input().strip()
    dq = deque()
    for m in mag:
        dq.append(int(m))
    magnetics[i] = dq # 0:N극, 1:S극

K = int(input())  # 자석을 회전시키는 횟수
for time in range(K):
    idx, r = map(int, input().split())  # 1: 시계, -1: 반시계
    # 회전하는 자석(idx)
    if idx == 1:
        temp_r = r
        temp = deepcopy(magnetics)
        temp[idx].rotate(r)
        for i in range(idx, 4):  # 뒤쪽 자석들
            if magnetics[i][2] == magnetics[i + 1][6]:
                break
            else:
                temp[i + 1].rotate(-temp_r)
                temp_r = -temp_r
        magnetics = deepcopy(temp)
    elif 2 <= idx <= 3:
        temp_r = r
        temp = deepcopy(magnetics)
        temp[idx].rotate(r)
        for i in range(idx, 4):  # 뒤쪽 자석들
            if magnetics[i][2] == magnetics[i+1][6]:
                break
            else:
                temp[i + 1].rotate(-temp_r)
                temp_r = -temp_r
        temp_r = r
        for i in range(idx, 1, -1):  # 앞쪽 자석들
            if magnetics[i][6] == magnetics[i - 1][2]:
                break
            else:
                temp[i - 1].rotate(-temp_r)
                temp_r = -temp_r
        magnetics = deepcopy(temp)
    elif idx == 4:
        temp_r = r
        temp = deepcopy(magnetics)
        temp[idx].rotate(r)
        for i in range(idx, 1, -1):  # 앞쪽 자석들
            if magnetics[i][6] == magnetics[i - 1][2]:
                break
            else:
                temp[i - 1].rotate(-temp_r)
                temp_r = -temp_r
        magnetics = deepcopy(temp)

# 점수 계산
point = 0
for idx in magnetics:
    up = magnetics[idx][0]
    if up == 1:
        point += 2 ** (idx-1)

print(f'{point}')
