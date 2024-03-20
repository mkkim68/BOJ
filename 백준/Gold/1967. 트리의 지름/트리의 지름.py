import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(now, cnt):
    global ans, d_point
    if ans < cnt:
        d_point = now
        ans = cnt
    for arr in adj[now]:
        to, w = arr[0], arr[1]

        # 이미 방문했다면 pass
        if visited[to]:
            continue

        visited[to] = 1
        dfs(to, cnt + w)
        visited[to] = 0


N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, c, w = map(int, input().split())
    adj[p].append([c, w])
    adj[c].append([p, w])

ans = 0
d_point = 0
visited = [0] * (N+1)

visited[1] = 1
dfs(1, 0)
visited[1] = 0
visited[d_point] = 1
dfs(d_point, 0)

print(ans)