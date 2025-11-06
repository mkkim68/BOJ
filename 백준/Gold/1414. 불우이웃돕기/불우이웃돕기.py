import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = 1e9

lengths = {'0': INF}
for i in range(1, 27):
    s = chr(i+96)
    lengths[s] = i

    l = chr(i+64)
    lengths[l] = i+26

N = int(input())
graphs = [list(input().strip()) for _ in range(N)]

total = 0
for i in range(N):
    for j in range(N):
        if lengths[graphs[i][j]] < INF:
            total += lengths[graphs[i][j]]
        graphs[i][j] = lengths[graphs[i][j]]

for k in range(N):
    for a in range(N):
        for b in range(N):
            graphs[a][b] = min(graphs[a][b], graphs[a][k] + graphs[k][b], graphs[b][a], graphs[b][k] + graphs[k][a])

pq = []
MST = [0] * N
sum_weight = 0
heappush(pq, (0, 0))
while pq:
    w, now = heappop(pq)

    if MST[now]:
        continue

    MST[now] = 1
    sum_weight += w

    for to in range(N):
        if graphs[now][to] == INF or MST[to]:
            continue

        heappush(pq, (graphs[now][to], to))

if 0 in MST:
    print(-1)
else:
    print(total - sum_weight)