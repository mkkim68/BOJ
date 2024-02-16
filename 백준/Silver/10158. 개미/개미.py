import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())


np = (p+t) % (2*w)
nq = (q+t) % (2*h)
if np > w:
    np = 2*w - np
if nq > h:
    nq = 2*h - nq
print(np, nq)