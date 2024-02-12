import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
table = deque(i for i in range(1, N+1))

print('<', end='')
while len(table) > 1:
    table.rotate(-K)
    print(table.pop(), end=', ')

print(table.pop(), end='>')