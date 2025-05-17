import sys
from collections import deque
from tokenize import endpats

input = sys.stdin.readline

N, L = map(int, input().split())
sticks = [list(map(int, input().split())) for _ in range(N)]
sticks.sort()

ans = 0
boundary = sticks[0][0]
for s, e in sticks:
    if s > boundary:
        boundary = s
    diff = e - boundary
    if diff%L == 0:
        cnt = diff//L
        boundary = e
    else:
        cnt = diff//L + 1
        boundary = e + (L-diff%L)
    ans += cnt

print(ans)