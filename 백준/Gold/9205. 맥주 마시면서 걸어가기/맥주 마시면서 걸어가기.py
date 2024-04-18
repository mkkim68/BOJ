import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    house = tuple(map(int, input().split()))
    convs = deque()
    beer = 20
    for _ in range(n):
        x, y = map(int, input().split())
        convs.append((x, y))
    festival = tuple(map(int, input().split()))

    q = deque([house])
    visited = set()
    while q:
        r, c = q.popleft()
        visited.add((r, c))
        if abs(festival[0]-r) + abs(festival[1]-c) <= 1000:
            print('happy')
            break
        for cr, cc in convs:
            if abs(cr-r) + abs(cc-c) <= 1000 and (cr, cc) not in visited:
                q.append((cr, cc))
    else:
        print('sad')

