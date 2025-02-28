import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(person):
    pq = []
    distances = [1e9] * (N+1)
    heappush(pq, (person, 0))
    distances[person] = 0
    while pq:
        now, cnt = heappop(pq)
        if distances[now] < cnt:
            continue

        distances[now] = cnt
        for next in edges[now]:
            if distances[next] <= cnt + 1:
                continue
            heappush(pq, (next, cnt+1))

    if 1e9 in distances[1:]:
        return 1e9
    else:
        return max(distances[1:])

N = int(input())
edges = [[] for _ in range(N+1)]
while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    edges[a].append(b)
    edges[b].append(a)

min_score = 1e9
candidates = []
for i in range(1, N+1):
    temp = dijkstra(i)
    if temp < min_score:
        min_score = temp
        candidates = [i]
    elif temp == min_score:
        candidates.append(i)

print(min_score, len(candidates))
print(*sorted(candidates))