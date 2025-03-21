import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
know_cnt, *knows = list(map(int, input().split()))

edges = [[] for _ in range(N+1)]
party = {i: set() for i in range(1, N+1)}
for m in range(1, M+1):
    p_cnt, *people = list(map(int, input().split()))

    for i in range(p_cnt-1):
        for j in range(i+1, p_cnt):
            edges[people[i]].append(people[j])
            edges[people[j]].append(people[i])

    for p in people:
        party[p].add(m)


def bfs(start):
    global visited
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        if now in visited:
            continue
        visited.add(now)
        for next in edges[now]:
            if next not in visited:
                q.append(next)
    return

visited = set()
for know in knows:
    if know not in visited:
        bfs(know)

ans = set()
for person in visited:
    for p in party[person]:
        ans.add(p)

print(M-len(ans))