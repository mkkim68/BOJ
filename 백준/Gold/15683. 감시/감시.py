import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline


def cctv1(row, col):
    delta = deque([(1,0), (-1,0), (0,1), (0,-1)])
    ans = []
    for dr, dc in delta:
        nr, nc = row + dr, col + dc
        temp = set()
        while 0 <= nr < N and 0 <= nc < M and office[nr][nc] != 6:
            if office[nr][nc] == 0:
                temp.add((nr, nc))
            nr, nc = nr + dr, nc + dc
        if temp:
            ans.append(temp)
    return ans


def cctv2(row, col):
    deltas = [deque([(1,0), (-1,0)]), deque([(0,1), (0,-1)])]  # 상하, 좌우
    ans = []
    for delta in deltas:
        temp = set()
        for dr, dc in delta:
            nr, nc = row + dr, col + dc
            while 0 <= nr < N and 0 <= nc < M and office[nr][nc] != 6:
                if office[nr][nc] == 0:
                    temp.add((nr, nc))
                nr, nc = nr + dr, nc + dc
        if temp:
            ans.append(temp)
    return ans


def cctv3(row, col):
    deltas = deque([(1, 0), (0, 1)]), deque([(0, 1), (-1, 0)]), deque([(-1,0), (0,-1)]), deque([(0,-1), (1, 0)])
    ans = []
    for delta in deltas:
        temp = set()
        for dr, dc in delta:
            nr, nc = row + dr, col + dc
            while 0 <= nr < N and 0 <= nc < M and office[nr][nc] != 6:
                if office[nr][nc] == 0:
                    temp.add((nr, nc))
                nr, nc = nr + dr, nc + dc
        if temp:
            ans.append(temp)
    return ans


def cctv4(row, col):
    deltas = deque([(1, 0), (0, 1), (-1,0)]), deque([(0, 1), (-1, 0), (0,-1)]), deque([(-1, 0), (0, -1), (1, 0)]), deque([(0, -1), (1, 0), (0, 1)])
    ans = []
    for delta in deltas:
        temp = set()
        for dr, dc in delta:
            nr, nc = row + dr, col + dc
            while 0 <= nr < N and 0 <= nc < M and office[nr][nc] != 6:
                if office[nr][nc] == 0:
                    temp.add((nr, nc))
                nr, nc = nr + dr, nc + dc
        if temp:
            ans.append(temp)
    return ans


def cctv5(row, col):
    delta = deque([(1, 0), (-1, 0), (0, 1), (0, -1)])
    ans = []
    temp = set()
    for dr, dc in delta:
        nr, nc = row + dr, col + dc
        while 0 <= nr < N and 0 <= nc < M and office[nr][nc] != 6:
            if office[nr][nc] == 0:
                temp.add((nr, nc))
            nr, nc = nr + dr, nc + dc
    ans.append(temp)
    return ans


N, M = map(int, input().split())
office = []
for _ in range(N):
    office.append(list(map(int, input().split())))

wall, cctv_len = 0, 0
points = {}
length = []
point = []
for r in range(N):
    for c in range(M):
        if 0 < office[r][c] < 6:
            cctv_len += 1
            a = office[r][c]
            if a == 1:
                points[(r, c)] = cctv1(r, c)
                if not point:
                    point.extend(cctv1(r,c))
                else:
                    if points[(r,c)]:
                        temp = []
                        for p in point:
                            for cctv in cctv1(r, c):
                                temp.append(p | cctv)
                        point = deepcopy(temp)
            elif a == 2:
                points[(r, c)] = cctv2(r, c)
                if not point:
                    point.extend(cctv2(r,c))
                else:
                    if points[(r,c)]:
                        temp = []
                        for p in point:
                            for cctv in cctv2(r, c):
                                temp.append(p | cctv)
                        point = deepcopy(temp)
            elif a == 3:
                points[(r,c)]= cctv3(r, c)
                if not point:
                    point.extend(cctv3(r,c))
                else:
                    if points[(r,c)]:
                        temp = []
                        for p in point:
                            for cctv in cctv3(r, c):
                                temp.append(p | cctv)
                        point = deepcopy(temp)
            elif a == 4:
                points[(r,c)] = cctv4(r, c)
                if not point:
                    point.extend(cctv4(r,c))
                else:
                    if points[(r,c)]:
                        temp = []
                        for p in point:
                            for cctv in cctv4(r, c):
                                temp.append(p | cctv)
                        point = deepcopy(temp)
            elif a == 5:
                points[(r, c)]= cctv5(r, c)
                if not point:
                    point.extend(cctv5(r,c))
                else:
                    if points[(r,c)]:
                        temp = []
                        for p in point:
                            for cctv in cctv5(r, c):
                                temp.append(p | cctv)
                        point = deepcopy(temp)
        elif office[r][c] == 6:
            wall += 1
        # print(r, c, point)

point.sort(key=lambda x:-len(x))
if point:
    ans = len(point[0])
    print(N * M - (wall + cctv_len + ans))
else:
    print(N * M - (wall + cctv_len))
