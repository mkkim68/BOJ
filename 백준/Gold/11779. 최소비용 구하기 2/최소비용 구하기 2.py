from heapq import heappop, heappush
import sys
input = sys.stdin.readline


def dijkstra(start):
    costs[start] = 0
    pq = []
    heappush(pq, (0, start, [start]))
    while pq:
        cost, now, path = heappop(pq)
        if costs[now] < cost:
            continue

        for arr in adj[now]:
            next, w = arr[0], arr[1]
            nc = w + cost
            if costs[next] <= nc:
                continue
            costs[next] = nc
            paths[next] = path + [next]
            heappush(pq, (nc, next, path + [next]))



N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append([e, w])
S, E = map(int, input().split())

costs = [1e9] * (N + 1)
paths = [0] * (N+1)
dijkstra(S)
min_cost = costs[E]

print(min_cost)
print(len(paths[E]))
print(*paths[E])