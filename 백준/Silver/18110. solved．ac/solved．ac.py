import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deq = deque()
for _ in range(n):
    deq.append(int(input()))

deq = deque(sorted(deq))

minmax = n / 100 * 15
if minmax - int(minmax) >= 0.5:
    minmax = int(minmax) + 1
else:
    minmax = int(minmax)

for _ in range(minmax):
    deq.pop()
    deq.popleft()

ans = 0
for i in range(n - 2*minmax):
    ans += deq.pop()
try:
    ans /= n - 2 * minmax
except:
    ans = 0

if ans - int(ans) >= 0.5:
    ans = int(ans) + 1
else:
    ans = int(ans)

print(ans)