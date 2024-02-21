import sys
from collections import deque
input = sys.stdin.readline

K = int(input())

d_dict = {}
dq = deque()
w_dq = deque()
for _ in range(6):
    # 동:1 서:2 남:3 북:4
    d, w = map(int, input().split())
    dq.append(d)
    w_dq.append(w)
    if d not in d_dict:
        d_dict[d] = w

while True:
    a = dq.popleft()
    b = dq.pop()
    if a in dq or b in dq:
        dq.appendleft(a)
        dq.append(b)
        dq.rotate(1)
        w_dq.rotate(1)
    else:
        dq.appendleft(a)
        dq.append(b)
        break

big = 1
if d_dict[1] > d_dict[2]:
    big *= d_dict[1]
else:
    big *= d_dict[2]

if d_dict[3] > d_dict[4]:
    big *= d_dict[3]
else:
    big *= d_dict[4]

small = w_dq[2] * w_dq[3]

print(K * (big-small))