import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, d = map(int, input().split())
    edges[a].append([b, 2 * d])
    edges[b].append([a, 2 * d])

# 늑대
wolf = [[1e9]*2 for _ in range(N+1)]  # fast, slow 따로
pq = []
heappush(pq, (0, 1, 0))  # time, node, 속도(0:빠름, 1:느림)
while pq:
    t, now, speed = heappop(pq)
    if wolf[now][speed] < t:
        continue

    for next, dt in edges[now]:
        if speed == 0:
            nt = t + dt // 2
        else:
            nt = t + dt * 2
        if wolf[next][not speed] <= nt:
            continue
        wolf[next][not speed] = nt
        heappush(pq, (nt, next, not speed))


# 여우
fox = [1e9] * (N+1)
pq = []
heappush(pq, (0, 1))
while pq:
    t, now = heappop(pq)
    if fox[now] < t:
        continue

    for next, dt in edges[now]:
        nt = t + dt
        if fox[next] <= nt:
            continue
        fox[next] = nt
        heappush(pq, (nt, next))

ans = 0
for i in range(2, N+1):
    if wolf[i][0] > fox[i] and wolf[i][1] > fox[i]:
        ans += 1

print(ans)