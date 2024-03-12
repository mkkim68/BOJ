import sys
from collections import deque
input = sys.stdin.readline


def dfs(r, c):
    global baby_size, feed
    q = deque()
    q.append([(r, c)])
    visited = [[0] * N for _ in range(N)]
    d = 0
    while q:
        cur_d = q.popleft()
        temp = deque()
        feeds = []
        for cur in cur_d:
            curr, curc = cur[0], cur[1]
            if visited[curr][curc] == 0:
                if 0 < space[curr][curc] < baby_size:
                    feeds.append((curr, curc))
                visited[curr][curc] = 1
                for dr, dc in delta:
                    nr, nc = curr + dr, curc + dc
                    if 0 <= nr < N and 0 <= nc < N and 0 <= space[nr][nc] <= baby_size and visited[nr][nc] == 0:
                        temp.append((nr, nc))
        if feeds:
            feeds.sort(key=lambda x:(x[0], x[1]))
            fr, fc = feeds[0][0], feeds[0][1]
            space[fr][fc] = 0
            feed += 1
            if feed == baby_size:
                baby_size += 1
                feed = 0
            return [d, fr, fc]  #  먹이를 먹는데 걸린 시간, 먹은 위치
        if temp:
            q.append(temp)
            d += 1
    return [-99]  # 먹이 못 먹는 상황

N = int(input())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            sr, sc = i, j  # 아기상어의 첫 위치
            space[i][j] = 0

baby_size = 2  # 처음 아기상어의 크기
curr, curc = sr, sc
delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
time = 0
feed = 0
while True:
    arr = dfs(curr, curc)
    if arr[0] == -99:
        print(time)
        break
    else:
        t, curr, curc = arr[0], arr[1], arr[2]
        time += t