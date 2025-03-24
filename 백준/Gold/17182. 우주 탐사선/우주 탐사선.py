import sys
input = sys.stdin.readline

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])



ans = 1e9
visited = [0] * N
visited[K] = 1
def dfs(prev, cnt, distance):
    global ans
    if distance >= ans:
        return

    if cnt == N:
        ans = min(ans, distance)
        return

    for to in range(N):
        if visited[to]:
            continue

        visited[to] = 1
        dfs(to, cnt+1, distance+graph[prev][to])
        visited[to] = 0

dfs(K, 1, 0)
print(ans)