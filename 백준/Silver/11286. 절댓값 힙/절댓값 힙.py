import sys
input = sys.stdin.readline


def enq(n):
    global last
    last += 1
    h[last] = n
    c = last
    p = c // 2
    while p >= 1 and (abs(h[p]) > abs(h[c]) or (abs(h[p]) == abs(h[c]) and h[p] > h[c])):
        h[p], h[c] = h[c], h[p]
        c = p
        p = c // 2


def deq():
    global last
    tmp = h[1]
    h[1] = h[last]
    h[last] = 0
    last -= 1
    p = 1
    c = p * 2
    while c <= last:
        if c+1 <= last and (abs(h[c]) > abs(h[c+1]) or (abs(h[c]) == abs(h[c+1]) and h[c] > h[c+1])):
            c += 1
        if abs(h[p]) > abs(h[c]):
            h[p], h[c] = h[c], h[p]
            p = c
            c = p * 2
        elif abs(h[p]) == abs(h[c]) and h[p] > h[c]:
            h[p], h[c] = h[c], h[p]
            p = c
            c = p * 2
        else:
            break
    return tmp


N = int(input())
h = [0] * (N+1)
last = 0
for i in range(1, N+1):
    x = int(input())
    if x != 0:
        enq(x)
    else:
        if last == 0:
            print(0)
        else:
            print(deq())
    # print(i, h)
