import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N, P, K = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(P):
    a, b, cost = map(int, input().split())
    edges[a].append((b, cost))
    edges[b].append((a, cost))


def check(limit):
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    pq = [(0, 1)]

    while pq:
        d, now = heappop(pq)
        if dist[now] < d: continue

        for next, cost in edges[now]:
            weight = 1 if cost > limit else 0
            if dist[next] > d + weight:
                dist[next] = d + weight
                heappush(pq, (dist[next], next))

    return dist[N] <= K


low, high = 0, 1000001
ans = -1

while low <= high:
    mid = (low + high) // 2
    if check(mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)