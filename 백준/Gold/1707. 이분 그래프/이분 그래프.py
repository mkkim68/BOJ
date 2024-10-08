import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    global flag, colors

    q = deque()
    q.append(start)
    colors[start] = 1
    while q and flag:
        now = q.popleft()

        for next in edges[now]:
            if colors[next] == colors[now]:
                flag = False
                return
            if colors[next] != 0:
                continue
            colors[next] = colors[now] * -1
            q.append(next)


K = int(input())
for tc in range(K):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)

    flag = True
    colors = [0] * (V + 1)
    for v in range(1, V+1):
        if not colors[v]:
            bfs(v)
        if not flag:
            break

    if flag:
        print("YES")
    else:
        print("NO")
