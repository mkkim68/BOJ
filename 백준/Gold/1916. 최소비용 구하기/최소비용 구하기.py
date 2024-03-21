from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijkstra(start):
    pq = []
    prices = [1e9] * (N+1)
    heappush(pq, (0, start))
    prices[start] = 0

    while pq:
        price, now = heappop(pq)

        if prices[now] < price:
            continue

        for to in adj[now]:
            next, w = to[0], to[1]
            new_price = price + w
            if prices[next] > new_price:
                prices[next] = new_price
                heappush(pq, (new_price, next))

    return prices[end]


N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append([e, w])

start, end = map(int, input().split())
ans = dijkstra(start)
print(ans)