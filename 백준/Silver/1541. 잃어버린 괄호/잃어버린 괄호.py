import sys
from collections import deque
input = sys.stdin.readline

A = input().strip()
B = A.split('-')

q = deque()
for num in B:
    if num.isdecimal():
        q.append(int(num))
    else:
        n = num.split('+')
        cnt = 0
        for i in n:
            cnt += int(i)
        q.append(cnt)

while len(q) > 1:
    n1 = q.popleft()
    n2 = q.popleft()
    q.appendleft(n1-n2)

print(q[0])


