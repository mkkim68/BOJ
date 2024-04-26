import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
ladders = {}
dp = [(i-2)//6+1 for i in range(101)]
for _ in range(N):
    s, e = map(int, input().split())
    ladders[s] = e

snakes = {}
for _ in range(M):
    s, e = map(int, input().split())
    snakes[s] = e

q = deque()
now = 1
q.append([now, 0])
visited = set()
delta = [1, 2, 3, 4, 5, 6]
while q:
    cur, dis = q.popleft()
    if cur == 100:
        print(dis)
        break
    if cur in visited:
        continue
    visited.add(cur)
    for d in delta:
        next = d + cur
        if next <= 100 and next not in visited:
            if next in ladders:
                q.append([ladders[next], dis+1])
                continue
            if next in snakes:
                q.append([snakes[next], dis+1])
                continue
            q.append([next, dis+1])

