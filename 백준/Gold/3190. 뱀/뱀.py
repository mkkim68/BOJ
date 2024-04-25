import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
apples = set()
for _ in range(K):
    apples.add(tuple(map(int, input().split())))

L = int(input())

# (1, 1) 부터 (N, N)
delta = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])  # rotate(1): 왼쪽 회전(L), rotate(-1): 오른쪽 회전(D)
r, c, dir = 1, 1, delta[0]
time, ans = 0, -1
body = deque([(1, 1)])
# commands = []
for _ in range(L):
    X, C = input().split()
    X = int(X)
    if ans == -1:
        for sec in range(time, X):
            time += 1
            dr, dc = dir[0], dir[1]
            nr, nc = dr + r, dc + c
            if 1<=nr<=N and 1<=nc<=N and (nr, nc) not in body:
                r, c = nr, nc
                body.appendleft((nr, nc))
                if (nr, nc) in apples:
                    apples.remove((nr, nc))
                else:
                    body.pop()
                # print(nr, nc, time)
                # print(body)
            else:
                if ans == -1:
                    ans = time
        if C == 'L':
            delta.rotate(1)
        elif C == "D":
            delta.rotate(-1)
        dir = delta[0]

while ans == -1:
    time += 1
    dr, dc = dir[0], dir[1]
    nr, nc = dr + r, dc + c
    if 1 <= nr <= N and 1 <= nc <= N and (nr, nc) not in body:
        r, c = nr, nc
        body.appendleft((nr, nc))
        if (nr, nc) in apples:
            apples.remove((nr, nc))
        else:
            body.pop()
        # print(body)
    else:
        ans = time
    # print(nr, nc, time)

print(ans)