import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
requests = list(map(int, input().split()))
total = int(input())

l, r = 0, max(requests)
ans = 0
while l <= r:
    m = (l + r) // 2
    temp = 0
    for req in requests:
        if req >= m:
            temp += m
        else:
            temp += req

        if temp > total:
            break

    if temp > total:
        r = m - 1
    else:
        ans = max(m, ans)
        l = m + 1

print(ans)