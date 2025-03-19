import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
pq = []
for i in range(N):
    heappush(pq, int(input()))

ans = 0
while len(pq) > 1:
    a = heappop(pq)
    b = heappop(pq)

    ans += a+b
    heappush(pq, a+b)

print(ans)