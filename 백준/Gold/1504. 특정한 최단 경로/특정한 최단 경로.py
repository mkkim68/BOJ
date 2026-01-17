import sys
from collections import deque
from heapq import heappop, heappush
input = sys.stdin.readline
INF = 1e9

N, E = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

v1, v2 = map(int, input().split())
def sol(start, sw, target):
    pq = []
    heappush(pq, (sw, start))
    distances = [INF] * (N+1)
    distances[start] = sw

    while pq:
        dis, now = heappop(pq)

        if distances[now] < dis:
            continue

        if now == target:
            return distances[now]

        for to, w in edges[now]:
            n_dis = dis + w
            if distances[to] <= n_dis:
                continue

            heappush(pq, (n_dis, to))
            distances[to] = n_dis

    return -1

arr1 = [1, v1, v2, N]
dis1 = 0
for i in range(3):
    temp = sol(arr1[i], dis1, arr1[i+1])
    if temp == -1:
        dis1 = INF
        break
    dis1 = temp

arr2 = [1, v2, v1, N]
dis2 = 0
for i in range(3):
    temp = sol(arr2[i], dis2, arr2[i+1])
    if temp == -1:
        dis2 = INF
        break
    dis2 = temp

if dis1 == dis2 == INF:
    print(-1)
else:
    print(min(dis1, dis2))