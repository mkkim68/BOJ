import sys
from collections import deque
input = sys.stdin.readline


def dfs(G, v):
    visited = [0]*(N+1)
    dfs_arr = []
    stack = [v]
    while stack:
        s = stack.pop()
        if not visited[s]:
            visited[s] = True
            dfs_arr.append(s)
        G[s].sort()
        for i in G[s]:
            if not visited[i]:
                stack.append(s)
                stack.append(i)
                break
    return dfs_arr


def bfs(G, v):
    visited = [0]*(N+1)
    bfs_arr = []
    queue = deque()
    queue.append(v)
    while queue:
        t = queue.popleft()
        if not visited[t]:
            visited[t] = True
            bfs_arr.append(t)
            G[t].sort()
            for i in G[t]:
                if not visited[i]:
                    queue.append(i)
    return bfs_arr


N, M, V = map(int, input().split())
arr = []
for i in range(M):
    arr.append(list(map(int, input().split())))

adj = [[] for _ in range(N+1)]
for i in range(M):
    n1, n2 = arr[i][0], arr[i][1]
    adj[n1].append(n2)
    adj[n2].append(n1)

a = dfs(adj, V)
b = bfs(adj, V)
print(*a)
print(*b)
