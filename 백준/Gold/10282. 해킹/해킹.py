import sys
from heapq import heappush, heappop
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n, d, c = map(int, input().split())
    edges = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        edges[b].append([a, s])

    cnt, time = 1, 0
    pq = []
    times = [1e9] * (n+1)
    heappush(pq, (c, 0))
    times[c] = 0
    while pq:
        now, t = heappop(pq)
        if times[now] < t:
            continue
        for next, w in edges[now]:
            n_time = t + w
            if times[next] <= n_time:
                continue
            times[next] = n_time
            heappush(pq, (next, n_time))

    time = 0
    for t in times:
        if t < 1e9:
            time = max(time, t)

    print(n+1 - times.count(1e9), time)
