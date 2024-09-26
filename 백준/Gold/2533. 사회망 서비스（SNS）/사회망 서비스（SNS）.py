import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(N-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

dp = [[0, 0] for _ in range(N+1)]


def sol(now):
    visited[now] = 1
    dp[now][0] = 1
    for node in edges[now]:
        if visited[node] == 0:
            sol(node)
            dp[now][1] += dp[node][0]
            dp[now][0] += min(dp[node][1], dp[node][0])

    return

sol(1)
print(min(dp[1]))