import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = deque(map(int, input().split()))

stack = []
last = 0
while arr:
    now = arr.popleft()
    if now == last + 1:
        last = now
        continue

    while stack:
        if stack[-1] == last + 1:
            last = stack[-1]
            stack.pop()
        else:
            break

    stack.append(now)

while stack:
    now = stack.pop()
    if now == last + 1:
        last = now
        continue
    else:
        print('Sad')
        break
else:
    print('Nice')