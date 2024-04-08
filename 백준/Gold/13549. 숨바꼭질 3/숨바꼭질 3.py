import sys
from collections import deque
from heapq import heappop, heappush
input = sys.stdin.readline

N, K = map(int, input().split())
# 걸을때 1초 순간이동 0초
times = [1e9] * 100001

pq = [(0, N)]
times[N] = 0
while pq:
    time, now = heappop(pq)
    if times[now] < time:
        continue

    times[now] = time
    nexts = [now-1, now+1]
    magic = now*2
    for next in nexts:
        if 0 <= next <= 100000:
            next_time = time + 1
            if next_time >= times[next]:
                continue
            times[next] = next_time
            heappush(pq, (next_time, next))
    if magic <= 100000:
        if time >= times[magic]:
            pass
        else:
            times[magic] = time
            heappush(pq, (time, magic))

print(times[K])