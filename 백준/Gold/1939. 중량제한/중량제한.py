import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    edges[A].append([B, C])
    edges[B].append([A, C])

S, E = map(int, input().split())

def dijkstra(target):
    pq = []
    distances = [0] * (N+1)
    heappush(pq, (0, S))
    while pq:
        dis, now = heappop(pq)

        if distances[now] > dis:
            continue

        for next, w in edges[now]:
            if w < target:
                continue

            if distances[next] >= w:
                continue

            distances[next] = max(w, dis)
            heappush(pq, (max(w, dis), next))

    if distances[E] >= target:
        return True
    else:
        return False

l, r = 1, 1000000001
ans = 0
while l <= r:
    m = (l + r) // 2

    if dijkstra(m):
        ans = max(ans, m)
        l = m + 1
    else:
        r = m - 1

print(ans)

