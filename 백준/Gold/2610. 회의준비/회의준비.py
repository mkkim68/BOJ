import sys
from collections import deque
input = sys.stdin.readline
INF = 1e9
N = int(input())
M = int(input())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

def bfs(s):
    q = deque()
    q.append(s)

    team = []
    while q:
        now = q.popleft()

        team.append(now)
        for next in edges[now]:
            if visited[next]:
                continue

            visited[next] = 1
            q.append(next)

    graphs = {j: {i: INF if i!=j else 0 for i in team} for j in team}
    for i in team:
        for j in edges[i]:
            if j in team:
                graphs[i][j] = 1
                graphs[j][i] = 1

    for k in team:
        for a in team:
            for b in team:
                graphs[a][b] = min(graphs[a][b], graphs[a][k]+graphs[k][b])

    min_cnt = INF
    leader = 0
    for i in team:
        max_time = 0
        for j in team:
            if graphs[i][j] > max_time:
                max_time = graphs[i][j]
        if max_time < min_cnt:
            min_cnt = max_time
            leader = i

    return leader

visited = [0] * (N+1)
cnt = 0
leaders = []
for i in range(1, N+1):
    if visited[i]:
        continue

    visited[i] = 1
    L = bfs(i)
    leaders.append(L)
    cnt += 1

leaders.sort()
print(cnt)
print(*leaders, sep='\n')
