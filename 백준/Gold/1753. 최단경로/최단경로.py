import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def dijkstra(start):
    times = [1e9] * (V+1)
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

    return times

V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]
K = int(input())
for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s].append([e, w])

ans = dijkstra(K)
for i in range(1, V+1):
    if ans[i] == 1e9:
        print('INF')
    else:
        print(ans[i])
