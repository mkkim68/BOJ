import sys
from collections import deque
input = sys.stdin.readline

N, K, M = map(int, input().split())
edges = [[] for _ in range(N+1+M)]
for i in range(N+1, N+M+1):
    info = list(map(int, input().split()))
    edges[i] = info
    for j in info:
        edges[j].append(i)

q = deque()
visited = [0] * (N+M+1)
q.append(1)
visited[1] = 1
while q:
    now = q.popleft()
    if now == N:
        print(visited[now])

    for next in edges[now]:
        if visited[next]:
            continue
        if next >= N+1:
            visited[next] = visited[now]
        else:
            visited[next] = visited[now] + 1
        q.append(next)

if visited[N] == 0:
    print(-1)