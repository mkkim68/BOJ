import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def dijkstra(start, end):
    times = [1e9] * (N+1)
    times[start] = 0
    pq = []
    heappush(pq, (0, start))
    while pq:
        time, now = heappop(pq)
        if times[now] < time:
            continue

        for to in adj[now]:
            next, weight = to[0], to[1]
            next_time = time + weight
            if times[next] <= next_time:
                continue
            times[next] = next_time
            heappush(pq, (next_time, next))

    return times[end]


N, M, X = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append([e, w])

ans = 0
for i in range(1, N+1):
    ans = max(ans, dijkstra(i, X) + dijkstra(X, i))

print(ans)