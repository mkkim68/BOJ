import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dq = deque()
for _ in range(N):
    now = list(map(int, input().split()))
    if now[0] == 1:
        dq.appendleft(now[1])
    elif now[0] == 2:
        dq.append(now[1])
    elif now[0] == 3:
        if dq:
            a = dq.popleft()
            print(a)
        else:
            print(-1)
    elif now[0] == 4:
        if dq:
            a = dq.pop()
            print(a)
        else:
            print(-1)
    elif now[0] == 5:
        print(len(dq))
    elif now[0] == 6:
        if dq:
            print(0)
        else:
            print(1)
    elif now[0] == 7:
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif now[0] == 8:
        if dq:
            print(dq[-1])
        else:
            print(-1)
