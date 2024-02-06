import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
d = deque()
command = []
for _ in range(N):
    command.append(str(input()[:-1]))

for c in command:
    if "push_front" in c:
        num = int(c.split(' ')[-1])
        d.append(num)
    elif "push_back" in c:
        num = int(c.split(' ')[-1])
        d.appendleft(num)
    elif c == "back":
        if len(d) > 0: print(d[0])
        else: print(-1)
    elif c == "front":
        if len(d) > 0: print(d[-1])
        else: print(-1)
    elif c == "size":
        print(len(d))
    elif c == "empty":
        if len(d) == 0: print(1)
        else: print(0)
    elif c == "pop_front":
        if len(d) > 0: print(d.pop())
        else: print(-1)
    elif c == "pop_back":
        if len(d) > 0: print(d.popleft())
        else: print(-1)

