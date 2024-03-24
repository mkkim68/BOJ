import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 1
visited = set()
q = deque([[A]])
flag = 0
while flag == 0:
    arr = q.popleft()
    temp = []
    if not arr:
        print(-1)
        break
    for now in arr:
        if B == now:
            print(cnt)
            flag = 1
            break
        a, b = now * 2, int(str(now) + '1')
        if a <= B and a not in visited:
            temp.append(a)
            visited.add(a)
        if b <= B and b not in visited:
            temp.append(b)
            visited.add(b)
    else:
        cnt += 1
        q.append(temp)
