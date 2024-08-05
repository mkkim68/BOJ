import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = []
post = (0, 0)
houses = set()
for i in range(N):
    now = list(input().strip())
    board.append(now)
    for j in range(N):
        if now[j] == 'P':
            post = (i, j)
        elif now[j] == 'K':
            houses.add((i, j))

heights = []
height_set = set()
for i in range(N):
    now = list(map(int, input().split()))
    heights.append(now)
    for n in now:
        height_set.add(n)

arr = sorted(list(height_set))
delta = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
def bfs(start):
    q = deque()
    q.append(start)
    visited = set()
    K = 0
    while q:
        now = q.popleft()
        if now in visited:
            continue
        r, c = now
        if heights[r][c] < arr[left] or heights[r][c] > arr[right]:
            continue
        visited.add(now)
        if now in houses:
            K += 1
        for dr, dc in delta:
            nr, nc = dr + r, dc + c
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                q.append((nr, nc))
    return K

left, right = 0, 0
answer = 1e9
while right < len(arr):
    while left <= right:
        temp = bfs(post)
        if temp >= len(houses):
            answer = min(answer, arr[right]-arr[left])
            left += 1
        else:
            break
    right += 1

print(answer)