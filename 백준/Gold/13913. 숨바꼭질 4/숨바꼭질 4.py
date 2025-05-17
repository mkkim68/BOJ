import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

MAX = max(N, K) * 2 + 2
visited = [0] * MAX
history = [0] * MAX

q = deque()
q.append([N, 0, -1])
while q:
    now, dis, prev = q.popleft()
    if visited[now]:
        continue

    visited[now] = dis
    history[now] = prev

    if now == K:
        print(visited[now])
        break

    n1, n2, n3 = now-1, now+1, now*2
    if 0 <= n1 < MAX and not visited[n1]:
        q.append([n1, dis+1, now])
    if 0 <= n2 < MAX and not visited[n2]:
        q.append([n2, dis+1, now])
    if 0 <= n3 < MAX and not visited[n3]:
        q.append([n3, dis+1, now])

route = []
now = K
while True:
    route.append(now)
    if now == N:
        break
    now = history[now]

route.reverse()
print(*route)