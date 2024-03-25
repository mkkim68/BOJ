import sys
input = sys.stdin.readline


def dfs(start):
    stack = [start]
    while stack:
        cur = stack.pop()
        if visited[cur] == 0:
            visited[cur] = 1
            for next in adj[cur]:
                if visited[next] == 0:
                    stack.append(next)


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

visited = [0] * (N+1)
cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)