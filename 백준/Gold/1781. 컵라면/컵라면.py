import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
arr = []
max_date = 0
for i in range(1, N+1):
    d, c = map(int, input().split())
    arr.append([d, c])

arr.sort()
heap = []

for d, c in arr:
    heappush(heap, c)
    if len(heap) > d:
        heappop(heap)

print(sum(heap))