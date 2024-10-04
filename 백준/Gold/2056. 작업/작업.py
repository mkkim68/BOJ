import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
work_time = {}
indegree = [0] * (N+1)
edges = [[] for _ in range(N+1)]


for i in range(1, N+1):
    time, *works = map(int, input().split())
    work_time[i] = time
    indegree[i] = works[0]

    for j in range(1, works[0]+1):
        now = works[j]
        edges[now].append(i)


dp = [0] * (N+1)
q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = work_time[i]

while q:
    now = q.popleft()
    for next in edges[now]:
        indegree[next] -= 1
        dp[next] = max(dp[now] + work_time[next], dp[next])
        if indegree[next] == 0:
            q.append(next)

print(max(dp))