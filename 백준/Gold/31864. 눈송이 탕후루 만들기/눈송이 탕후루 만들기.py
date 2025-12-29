import sys
from math import gcd
from collections import defaultdict
from bisect import bisect_right
input = sys.stdin.readline

def normalize(x, y):
    dx = x
    dy = y
    g = gcd(abs(x), abs(y))
    dx //= g
    dy //= g
    return dx, dy

N, M = map(int, input().split())
lines = defaultdict(list)

for _ in range(N):
    x, y = tuple(map(int, input().split()))
    dx, dy = normalize(x, y)
    lines[(dx, dy)].append(x**2 + y**2)

for k in lines:
    lines[k].sort()

ans = 0
for i in range(M):
    ex, ey = map(int, input().split())
    dx, dy = normalize(ex, ey)
    d = ex**2 + ey**2
    cnt = bisect_right(lines[(dx, dy)], d)
    ans = max(ans, cnt)

print(ans)