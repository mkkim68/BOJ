import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

V = int(input())
edges = [[] for _ in range(V+1)]

for _ in range(V):
    node, *arr, last = map(int, input().split())
    for i in range(0, len(arr), 2):
        next, weight = arr[i], arr[i+1]
        edges[node].append([next, weight])

visited = [-1] * (V+1)
visited[1] = 0

def dfs(node, dist):
    for v, d in edges[node]:
        cal_dist = dist + d
        if visited[v] == -1:
            visited[v] = cal_dist
            dfs(v, cal_dist)
    return

dfs(1, 0)
tmp = [0, 0]

for i in range(1, V+1):
    if visited[i] > tmp[1]:
        tmp[1] = visited[i]
        tmp[0] = i

visited = [-1] * (V+1)
visited[tmp[0]] = 0
dfs(tmp[0], 0)

print(max(visited))