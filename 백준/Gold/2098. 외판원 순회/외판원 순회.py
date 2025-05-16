import sys
input = sys.stdin.readline

N = int(input())
INF = int(1e9)
graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * (1 << N) for _ in range(N)]

def dfs(start, visited):
    if visited == (1 << N) - 1:
        return graph[start][0] if graph[start][0] != 0 else INF

    if dp[start][visited] != -1:
        return dp[start][visited]

    min_cost = INF
    for i in range(1, N):
        if visited & (1 << i):
            continue
        if graph[start][i] == 0:
            continue
        cost = dfs(i, visited | (1 << i)) + graph[start][i]
        if cost < min_cost:
            min_cost = cost

    dp[start][visited] = min_cost
    return min_cost

ans = dfs(0, 1)

print(ans)
