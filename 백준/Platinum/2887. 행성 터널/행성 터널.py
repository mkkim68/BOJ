import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


N = int(input())
planets = []
planet_idx = {}
for i in range(N):
    x, y, z = map(int, input().split())
    planets.append((x, y, z))
    planet_idx[(x, y, z)] = i
parents = [i for i in range(N)]
adj = []  # 0번 행성부터 N-1번 행성까지 간선 연결
planets.sort(key=lambda x:x[0])
for i in range(N-1):
    p1, p2 = planets[i], planets[i+1]
    w = min(abs(p1[0]-p2[0]),abs(p1[1]-p2[1]),abs(p1[2]-p2[2]))
    adj.append([planet_idx[p1], planet_idx[p2], w])

planets.sort(key=lambda x:x[1])
for i in range(N-1):
    p1, p2 = planets[i], planets[i+1]
    w = min(abs(p1[0]-p2[0]),abs(p1[1]-p2[1]),abs(p1[2]-p2[2]))
    adj.append([planet_idx[p1], planet_idx[p2], w])

planets.sort(key=lambda x:x[2])
for i in range(N-1):
    p1, p2 = planets[i], planets[i+1]
    w = min(abs(p1[0]-p2[0]),abs(p1[1]-p2[1]),abs(p1[2]-p2[2]))
    adj.append([planet_idx[p1], planet_idx[p2], w])

adj.sort(key=lambda x: x[2])
cnt = 0
total = 0
for u, v, w in adj:
    if find_set(u) != find_set(v):
        cnt += 1
        union(u, v)
        total += w

print(total)