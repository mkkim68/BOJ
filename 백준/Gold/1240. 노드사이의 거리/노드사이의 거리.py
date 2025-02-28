import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, d = map(int, input().split())
    edges[a].append([b, d])
    edges[b].append([a, d])

for _ in range(M):
    s, e = map(int, input().split())
    q = deque()
    visited = [0] * (N+1)
    q.append(s)
    while q:
        now = q.popleft()
        if now == e:
            print(visited[now])

        for next, dis in edges[now]:
            if visited[next]:
                continue
            visited[next] = visited[now] + dis
            q.append(next)

