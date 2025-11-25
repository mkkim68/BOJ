import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

answer = sorted(arr)
q = deque()
visited = set()
q.append([arr, 0])
while q:
    now, cnt = q.popleft()
    if now == answer:
        print(cnt)
        break

    if tuple(now) in visited:
        continue

    visited.add(tuple(now))

    for i in range(N-K+1):
        temp = now[i:i+K]
        temp.reverse()
        next = now[:i] + temp + now[i+K:]
        q.append([next, cnt+1])
else:
    print(-1)