import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
edges = [list(map(int, input().split())) for _ in range(N)]
cities = list(map(int, input().split()))

q = deque()
q.append(cities[0]-1)
visited = [0] * N
while q:
    now = q.popleft()
    visited[now] = 1
    for i in range(N):
        if i != now and edges[now][i]:
            if visited[i]:
                continue
            q.append(i)

for c in cities:
    if not visited[c-1]:
        print("NO")
        break
else:
    print("YES")