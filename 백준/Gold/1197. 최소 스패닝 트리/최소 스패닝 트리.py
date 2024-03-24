import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def prim(start):
    visited = [0] * (V+1)
    pq = []
    sum_weight = 0
    heappush(pq, (0, start))
    while pq:
        weight, now = heappop(pq)

        if visited[now]:
            continue

        visited[now] = 1
        sum_weight += weight

        for next in adj[now]:
            to, w = next[0], next[1]
            if visited[to]:
                continue

            heappush(pq, (w, to))

    return sum_weight


V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s].append([e, w])
    adj[e].append([s, w])

ans = prim(1)
print(ans)