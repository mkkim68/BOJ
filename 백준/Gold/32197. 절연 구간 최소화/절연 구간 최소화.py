import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    edges[s].append([e, t])
    edges[e].append([s, t])

A, B = map(int, input().split())

INF = 1e9
dist = [[INF, INF] for _ in range(N+1)]
q = deque()
q.append([A, 0])
q.append([A, 1])
dist[A][0] = 0
dist[A][1] = 0

while q:
    now, way = q.popleft()

    for n, t in edges[now]:
        cost = abs(way-t)
        next_cnt = dist[now][way] + cost

        if dist[n][t] <= next_cnt:
            continue

        dist[n][t] = next_cnt
        if cost == 0:
            q.appendleft([n, t])
        else:
            q.append([n, t])


print(min(dist[B]))